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
    '/': 'favs_def',  # liked songs also, not shuffled (50 first songs)
    '*': 'favs_shuffle',  # favourite list, shuffled (50 random songs)
    '+': 'album',  # play album of current track playing
    # other playlists here
    # these are just my private ones
    '7': 'https://open.spotify.com/playlist/7oRDKW0qLCCTL4kdB9IyAH',  # damn this is good
    '8': 'https://open.spotify.com/playlist/2xGIJmGOGjXjgNZvaDz5MI',  # favourites of favourites
    '9': 'https://open.spotify.com/playlist/3sOHkO8mkdH0jULLxYLrgL',  # once upon a time
    '4': 'https://open.spotify.com/playlist/25BINn4b9lSfdo3PdGa8pZ',  # beautiful
    '5': 'https://open.spotify.com/playlist/7vRTWf5LdQoE9Kxe9JBL5O',  # trop calme
    '6': 'https://open.spotify.com/playlist/5qpQ3ihZ2GgDhfjXVy4A1B',  # etc
    '1': 'https://open.spotify.com/playlist/022hSssDIUrggKAI27F7ms',  # Party mit Mia und Lars
    '2': 'https://open.spotify.com/playlist/0qJt1pMG8QDQAkQLcaedAz',  # PM
    '3': 'https://open.spotify.com/playlist/2xwBNfyo360de2o2Mf4dmM',  # groovy tracks
    '0': 'https://open.spotify.com/playlist/37i9dQZEVXcMAZ3hwyicGi',  # Dein Mix der Woche
}
