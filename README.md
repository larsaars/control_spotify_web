# control spotify web rpi
Control spotify playback via web api and by receiving specific key strokes from keyboard (using a raspberry pi).

## install on linux
* spotify secrets
  * create file `spotify_secrets.txt`
  * create spotify dev account (need premium) and create app [here](https://developer.spotify.com/dashboard/login)
  * in app spotify app, go to edit settings > redirect uris > paste: `http://localhost:8888/callback` > click add > save
* `pip3 install -r requirements.txt`
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
DEL | mute
\* | restore volume after muting
/ | set volume to 10
0 | disable shuffle
1 | enable shuffle
SPACE | disable repeat
. | enable repeat track
