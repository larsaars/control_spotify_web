# the permission scope needed from spotify to be able to control playback etc.
PERMISSION_SCOPE = 'user-read-currently-playing user-modify-playback-state user-read-playback-state user-library-read'

# the standard volume
PREFERRED_VOLUME = 13
# the clap time difference
CLAP_TIME_DIFF = 0.4
# name of standard playing spotify connect device
PREFERRED_DEV_NAME = '237'
# name of city you live in
CITY_NAME = 'Regensburg'
# your language
LANGUAGE = 'EN'

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
    '-': 'artist',  # play more from artist of current playback
    # other playlists here
    # these are just my private ones
    '7': 'https://open.spotify.com/playlist/7oRDKW0qLCCTL4kdB9IyAH',  # damn this is good
    '8': 'https://open.spotify.com/playlist/2xGIJmGOGjXjgNZvaDz5MI',  # favourites of favourites
    '9': 'https://open.spotify.com/playlist/3sOHkO8mkdH0jULLxYLrgL',  # once upon a time
    '4': 'https://open.spotify.com/playlist/25BINn4b9lSfdo3PdGa8pZ',  # beautiful
    '<65437>': 'https://open.spotify.com/playlist/7vRTWf5LdQoE9Kxe9JBL5O',  # trop calme " button equals 5
#    '6': 'https://open.spotify.com/playlist/5qpQ3ihZ2GgDhfjXVy4A1B',  # etc
    '6': 'https://open.spotify.com/playlist/022hSssDIUrggKAI27F7ms',  # Party mit Mia und Lars
    '1': 'https://open.spotify.com/playlist/09eenxkQvsOrjQ67ljO9Oj',  # morning vibes
    '2': 'https://open.spotify.com/playlist/3SSSi0wkFSryrwflntZxKk',  # dramatic | whatever (day)
    '3': 'https://open.spotify.com/playlist/6nJKp3sUKFf3QfFdUlQJaB',  # good vibes (evening)
#    '1': 'https://open.spotify.com/playlist/022hSssDIUrggKAI27F7ms',  # Party mit Mia und Lars
#    '2': 'https://open.spotify.com/playlist/5coEobygUtc3VbOWZRCjtB',  # usw
#    '3': 'https://open.spotify.com/playlist/2xwBNfyo360de2o2Mf4dmM',  # groovy tracks
    '0': 'https://open.spotify.com/playlist/7Inx0D6rxoGeBTxuLjTzpI',  # session
    'Key.space': 'https://open.spotify.com/playlist/37i9dQZEVXcMAZ3hwyicGi',  # Dein Mix der Woche
    ',': 'https://open.spotify.com/playlist/37i9dQZF1Epm7edhYFruiz',  # On Repeat
    'Key.enter': 'https://open.spotify.com/playlist/37i9dQZF1EfLWEaldb43et',  # Daily Drive
    'Key.backspace': 'https://open.spotify.com/playlist/37i9dQZF1EnOBYmteT8p3O',  # Daily Podcasts
}
