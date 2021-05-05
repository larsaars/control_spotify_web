from login_spotify import spotify
from pynput.keyboard import Listener as KeyboardListener
from pynput.keyboard import KeyCode, Key

# variables
saved_volume = 10
preferred_device_id = '3c331613a26f366446dd2bb9297a8b4104e340d5'


# utility functions
def cur_volume() -> int:
    return int(spotify.current_playback()['device']['volume_percent'])


def cur_ms() -> int:
    return int(spotify.current_playback()['progress_ms'])


def char(key_code: str):
    return KeyCode.from_char(key_code)


# this is called when a button is pressed;
# wrap in try catch to never exit the program accidentally
def on_press(k):
    try:
        on_press_try(k)
    except:
        pass


# actions on key presses
def on_press_try(k):
    global saved_volume

    if k == char('q'):  # q: quit process
        keyboard_listener.stop()
    elif k == Key.enter:  # enter: play / pause
        if spotify.current_playback()['is_playing']:
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
    elif k == Key.backspace:  # DEL: mute
        # save volume for restoring
        saved_volume = cur_volume()
        # set vol to zero
        spotify.volume(volume_percent=0)
    elif k == char('*'):  # *: restore volume after mute
        spotify.volume(volume_percent=saved_volume)
    elif k == char('/'):
        spotify.start_playback(device_id=preferred_device_id)
        spotify.volume(volume_percent=10)
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


keyboard_listener = KeyboardListener(on_press=on_press)
# start listening and join thread
keyboard_listener.start()
keyboard_listener.join()
