# the permission scope needed from spotify to be able to control playback etc.
PERMISSION_SCOPE = 'user-read-currently-playing user-modify-playback-state user-read-playback-state user-library-read'

# the standard volume
PREFERRED_VOLUME = 13
# name of standard playing spotify connect device
PREFERRED_DEV_NAME = '237'

# dict with all urls to key press and playlist after pressing playlist select button ('/')

"""
here you can put:
- album links
- track links
- playlist links
in the format of an browser url: ex.: "https://open.spotify.com/playlist/PLAYLIST_ID"
or the format of a spotify url: ex.: "spotify:playlist:PLAYLIST_ID"
"""

PLAYLIST_URLS = {
    '1': 'favs_def',  # liked songs also, not shuffled (50 first songs)
    '2': 'favs_shuffle',  # favourite list, shuffled (50 random songs)
    '3': 'album',  # play album of current track playing
    # other playlists here
    '4': 'https://open.spotify.com/playlist/022hSssDIUrggKAI27F7ms'
}
