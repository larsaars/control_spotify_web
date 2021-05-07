# control spotify web rpi
Control spotify playback via web api and by receiving specific key strokes from keyboard (using a raspberry pi, assuming usage of raspotify).

## install on linux
* spotify secrets
  * create file `spotify_secrets.txt`
  * create spotify dev account (need premium) and create app [here](https://developer.spotify.com/dashboard/login)
  * in app spotify app, go to edit settings > redirect uris > paste: `http://localhost:8888/callback` > click add > save
* `sudo pip3 install -r requirements.txt`
* `sudo python3 main.py`

## shortcuts
shortcut | behaviour
--- | ---
q | quit process
ENTER | play / pause
6 | next song
4 | last song
8 | seek song +10s
2 | seek song -10s
\+ | volume ++
\- | volume --
BACKSPACE | set volume to preferred volume
0 | disable shuffle
1 | enable shuffle
SPACE | disable repeat
. | enable repeat track
\* | ensure preferred device is connected
/ | switch to start playlist mode

## switch playlist mode shortcuts
After pressing `/` and pressing one of the buttons in the table has the defined behaviour.

shortcut | behaviour
--- | ---
/ | play first songs from liked songs (max. 50 songs[^1])
\* | shuffle liked songs (max. 50 songs[^1])
\+ | play the album of current song
OTHER | all other keys are defined in config.py file and can be set to other playlists, albums, tracks etc.


[^1]: 50 songs are the limit in since the liked songs list is not treated as a playlist by Spotify, and the API can only receive 50 song uris.
