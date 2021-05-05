import os

import spotipy
from spotipy import SpotifyOAuth

# read the credentials
with open('spotify_secrets.txt', 'r') as file:
    content = file.read().splitlines()
    client_id = content[0]
    client_secret = content[1]

# set as env variables
os.environ['SPOTIPY_CLIENT_ID'] = client_id
os.environ['SPOTIPY_CLIENT_SECRET'] = client_secret
os.environ['SPOTIPY_REDIRECT_URI'] = 'http://localhost:8888/callback'

# the permission scope needed
scope = 'user-read-currently-playing user-modify-playback-state user-read-playback-state'

# login
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
