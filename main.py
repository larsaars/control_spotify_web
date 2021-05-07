import os
import random
from time import sleep

from config import *
from login_spotify import spotify
from pynput.keyboard import Listener as KeyboardListener
from pynput.keyboard import KeyCode, Key

# variables
select_playlist = False


# utility functions
def ceildiv(a, b):
    return -(-a // b)


def cur_volume() -> int:
    return int(spotify.current_playback()['device']['volume_percent'])


def cur_ms() -> int:
    return int(spotify.current_playback()['progress_ms'])


def char(key_code: str):
    return KeyCode.from_char(key_code)


def is_playing() -> bool:
    playback = spotify.current_playback()
    if playback is None:
        return False
    else:
        return playback['is_playing']


# this is called when a button is pressed;
# wrap in try catch to never exit the program accidentally
def on_press(k):
    try:
        on_press_try(k)
    except Exception as e:
        print(e)


# start playback of favourites list as liked songs is not treated as playlist
def start_favourites_playback(shuffle: bool):
    # this list will contain all liked songs ids
    liked_songs = []
    # if is shuffling, read out all songs and shuffle this list,
    # then transmit 50 first items of shuffled list
    if shuffle:
        # read out liked songs

        # get number of liked songs
        num_of_favs = int(spotify.current_user_saved_tracks(limit=1)['total'])
        # with offset of 20, run this many times
        # loop through them and get offset
        for i in range(ceildiv(num_of_favs, 20)):
            tracks_obj = spotify.current_user_saved_tracks(limit=20, offset=(i * 20))
            # loop through items list
            for track_item in tracks_obj['items']:
                liked_songs.append(track_item['track']['uri'])

        # shuffle list
        random.shuffle(liked_songs)

        # play first 50 of these songs (limit)
        spotify.start_playback(uris=liked_songs[:50])
    else:
        # just read out first 50 songs of fav list, prepare links
        # and play them
        for track_item in spotify.current_user_saved_tracks(limit=50)['items']:
            liked_songs.append(track_item['track']['uri'])

        # start playing liked songs
        spotify.start_playback(uris=liked_songs)


# ensure PREFERRED_DEV_NAME is connected and playing
def ensure_device():
    # list number of devices
    devices = spotify.devices()['devices']

    # there are no active or inactive devices
    # so restart raspotify service
    if len(devices) == 0:
        os.system('sudo systemctl restart raspotify.service')
        # then wait some seconds
        sleep(3)

    pref_dev = None
    for device in devices:
        if device['name'] == PREFERRED_DEV_NAME:
            pref_dev = device['id']
            break

    if pref_dev is not None:
        spotify.transfer_playback(device_id=pref_dev, force_play=True)


# play album of currently playing song
def play_album_current_track():
    playback = spotify.current_playback()
    if playback is not None:
        spotify.start_playback(context_uri=playback['item']['album']['uri'])


# play more by the artist of current track
def play_artist_current_track():
    playback = spotify.current_playback()
    if playback is not None:
        spotify.start_playback(context_uri=playback['item']['artists'][0]['uri'])


# actions on key presses
def on_press_try(k):
    global select_playlist

    # print('\n', k)

    # if select playlist mode is true, listen to the next key
    if select_playlist:
        select_playlist = False
        # get the playlist from dict
        playlist_url = PLAYLIST_URLS.get(str(k).strip('\''), 'none')
        # if this is a valid key in the dict, play the playlist
        if playlist_url != 'none':
            if playlist_url == 'favs_def':
                start_favourites_playback(False)
            elif playlist_url == 'favs_shuffle':
                start_favourites_playback(True)
            elif playlist_url == 'album':
                play_album_current_track()
            elif playlist_url == 'artist':
                play_artist_current_track()
            else:
                spotify.start_playback(context_uri=playlist_url)
        return

    if k == char('q'):  # q: quit process
        keyboard_listener.stop()
    elif k == Key.enter:  # enter: play / pause
        if is_playing():
            spotify.pause_playback()
        else:
            spotify.start_playback()
    elif k == char('6'):  # 6: next song
        spotify.next_track()
    elif k == char('4'):  # 4: last song
        spotify.previous_track()
    elif k == char('+'):  # +: volume ++
        # get current volume and the new
        vol = cur_volume()
        vol_new = vol + 2
        # if volume is already at max, do nothing
        if vol == 100:
            return

        #  if new volume is over 100, set vol_new to max
        spotify.volume(volume_percent=min(vol_new, 100))
    elif k == char('-'):  # -: volume --
        # get current volume and the new
        vol = cur_volume()
        vol_new = vol - 2
        # if volume is already at min, do nothing
        if vol == 0:
            return

        # if new volume is under 0, set vol_new to min
        spotify.volume(volume_percent=max(vol_new, 0))
    elif k == Key.backspace:  # DEL: set volume to PREFERRED_VOLUME
        spotify.volume(volume_percent=PREFERRED_VOLUME)
    elif k == char('*'):  # *: ensure preferred device is connected and playing
        ensure_device()
    elif k == char('0'):  # 0: disable shuffle
        spotify.shuffle(state=False)
    elif k == char('1'):  # 1: enable shuffle
        spotify.shuffle(state=True)
    elif k == char('8'):  # 8: seek song ++
        spotify.seek_track(position_ms=cur_ms() + 10000)
    elif k == char('2'):  # 2: seek song --
        spotify.seek_track(position_ms=max(0, cur_ms() - 10000))
    elif k == Key.space:  # SPACE: repeat track off
        spotify.repeat(state='off')
    elif k == char(',') or k == char('.'):  # .: repeat track on
        spotify.repeat(state='track')
    elif k == char('/'):  # /: switch playlist from dictionary
        select_playlist = True


keyboard_listener = KeyboardListener(on_press=on_press)
# start listening and join thread
keyboard_listener.start()
keyboard_listener.join()
