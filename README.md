# control spotify web
control spotify playback via web api and by receiving specific key strokes from keyboard

## install on linux
* spotify secrets
  * create file `spotify_secrets.txt`
  * create spotify dev account (need premium) and create app [here](https://developer.spotify.com/dashboard/login)
  * in app spotify app, go to edit settings > redirect uris > paste: `http://localhost:8888/callback` > click add > save
* `pip3 install -r requirements.txt`
