# spotbot
use currently playing track in spotify as slack status message

## Requirements
- pip install slackclient
- pip install spotipy

_Note: Spotipy does not currently support the [Currently Playing API](https://developer.spotify.com/web-api/get-the-users-currently-playing-track/). I've implemented [this PR](https://github.com/plamere/spotipy/pull/181) in my localenv for now._ 
