import os
import random
from time import sleep

from config import *
from login_spotify import spotify
from restart_raspotify import restart_rapotify_service


def ceildiv(a, b):
    return -(-a // b)


def cur_volume():
    return int(spotify.current_playback()['device']['volume_percent'])


def cur_ms():
    return int(spotify.current_playback()['progress_ms'])


def is_playing():
    playback = spotify.current_playback()
    if playback is None:
        return False
    else:
        return playback['is_playing']


# start playback of favourites list as liked songs is not treated as playlist
def start_favourites_playback(shuffle):
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
        restart_rapotify_service()
        os.system('sudo systemctl restart raspotify.service')
        # then wait some seconds
        sleep(8)

    pref_dev = None
    for device in devices:
        if device['name'] == PREFERRED_DEV_NAME:
            pref_dev = device['id']
            break

    if pref_dev is not None:
        # start playback
        spotify.transfer_playback(device_id=pref_dev, force_play=True)
        # set volume to preferred volume
        spotify.volume(volume_percent=PREFERRED_VOLUME)


# execute this method with try catch
def try_ensure_device():
    try:
        ensure_device()
    except Exception as e:
        print('ensuring device failed: ', e)


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
