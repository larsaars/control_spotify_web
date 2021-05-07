from config import *
from login_spotify import spotify
from pynput.keyboard import Listener as KeyboardListener
from pynput.keyboard import KeyCode, Key

# variables
select_playlist = False


# utility functions
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


# ensure PREFERRED_DEV_NAME is connected
def ensure_device():
    playback = spotify.current_playback()
    if playback is not None:
        spotify.pause_playback(device_id=playback['device']['id'])

    pref_dev = None
    for device in spotify.devices()['devices']:
        if device['name'] == PREFERRED_DEV_NAME:
            pref_dev = device['id']
            break

    if pref_dev is not None:
        spotify.transfer_playback(device_id=pref_dev, force_play=True)


# actions on key presses
def on_press_try(k):
    global select_playlist

    # if select playlist mode is true, listen to the next key
    if select_playlist:
        select_playlist = False
        # get the playlist from dict
        playlist_url = PLAYLIST_URLS.get(str(k).strip('\''), 'none')
        # if this is a valid key in the dict, play the playlist
        if playlist_url != 'none':
            spotify.pause_playback()
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
    elif k == char('*'):  # *: ensure device
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
    elif k == char('.'):  # .: repeat track on
        spotify.repeat(state='track')
    elif k == char('/'):  # /: switch playlist from dictionary
        select_playlist = True


keyboard_listener = KeyboardListener(on_press=on_press)
# start listening and join thread
keyboard_listener.start()
keyboard_listener.join()
