import traceback

from pynput.keyboard import KeyCode, Key
from pynput.keyboard import Listener as KeyboardListener

from say_weather import *
from spotify_tools import *

# variables
select_playlist, select_weather = False, False


def char(key_code: str):
    return KeyCode.from_char(key_code)


# this is called when a button is pressed;
# wrap in try catch to never exit the program accidentally
def on_press(k):
    try:
        on_press_try(k)
    except Exception:
        # print the error
        traceback.print_exc()
        # try ensure device
        try_ensure_device()


# actions on key presses
def on_press_try(k):
    global select_playlist, select_weather

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

    # if select weather
    if select_weather:
        select_weather = False

        if k == char('7'):
            say_weather_now()
        elif k == char('8'):
            say_sunrise_set()
        elif k == char('1'):
            say_weather_tomorrow_short()
        elif k == char('2'):
            say_weather_tomorrow_extra()
        elif k == char('3'):
            say_weather_next_days()

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
        try_ensure_device()
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
    elif k == char('7'):  # 7: switch weather statement (tell weather)
        select_weather = True


if __name__ == '__main__':
    # init the keyboard listener
    keyboard_listener = KeyboardListener(on_press=on_press)
    # start listening and join thread
    keyboard_listener.start()
    keyboard_listener.join()
