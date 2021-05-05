from login_spotify import spotify
from msvcrt import getch
from time import sleep

special = False


def cur_volume() -> int:
    return int(spotify.current_playback()['device']['volume_percent'])


while True:
    # get the key
    key = ord(getch())
    print(key)

    # on key execute specific actions
    if key == 13:  # enter: play / pause
        if spotify.current_playback()['is_playing']:
            spotify.pause_playback()
        else:
            spotify.start_playback()
    elif key == 54:  # 6: next song
        spotify.next_track()
    elif key == 52:  # 4: last song
        spotify.previous_track()
    elif key == 43:  # +: volume ++
        # get current volume and the new
        vol = cur_volume()
        vol_new = vol + 2
        # if volume is already at max, do nothing
        if vol == 100:
            continue

        #  if new volume is over 100, set vol_new to max
        spotify.volume(volume_percent=min(vol_new, 100))
    elif key == 45:  # -: volume --
        # get current volume and the new
        vol = cur_volume()
        vol_new = vol - 2
        # if volume is already at min, do nothing
        if vol == 0:
            continue

        # if new volume is under 0, set vol_new to min
        spotify.volume(volume_percent=max(vol_new, 0))
    elif key == 8:  # DEL: mute
        spotify.volume(volume_percent=0)
    elif key == 224:  # Special keys (arrows, f keys, ins, del, etc.)
        # so has to get next ch to know what has been the special action
        key = ord(getch())
        print(key)
