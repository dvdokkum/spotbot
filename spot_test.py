import sys
import os
import auth_keys
import spotipy
import spotipy.util as util

scope = 'user-read-currently-playing'
client_id = auth_keys.SPOTIPY_CLIENT_ID
client_secret = auth_keys.SPOTIPY_CLIENT_SECRET
redirect_url = auth_keys.SPOTIPY_REDIRECT_URL

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print "Usage: %s username" % (sys.argv[0],)
    sys.exit()

token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_url)

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.currently_playing()
    track_name = results['item']['name']
    artist_name = results['item']['artists'][0]['name']
    is_playing = results['is_playing']
    if is_playing == True:
        print is_playing
        print "Now Playing: " + track_name + " by " + artist_name
    else: print "Nothing Playing..."
else:
    print "Can't get token for", username
