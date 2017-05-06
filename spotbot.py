import sys
import os
import time
import auth_keys
import spotipy
import spotipy.util as util

from slackclient import SlackClient

#init slack
slack_client = SlackClient(auth_keys.SLACK_BOT_TOKEN)
status_emoji = ":musical_note:"

#init spotify
scope = 'user-read-currently-playing'
client_id = auth_keys.SPOTIPY_CLIENT_ID
client_secret = auth_keys.SPOTIPY_CLIENT_SECRET
redirect_url = auth_keys.SPOTIPY_REDIRECT_URL
username = auth_keys.SPOTIFY_USERNAME
token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_url)

poll_interval = 20
clear_status = '{"status_text":"","status_emoji":""}'

"""
todo: 
- add proper error handling
- allow spotify to refresh tokens
"""
def main():
	last_id = 0
	while True:
		if token:
			sp = spotipy.Spotify(auth=token)
			results = sp.currently_playing()
			is_playing = results['is_playing']
			track_id = results['item']['id']
			#print is_playing
			#print track_id
			if is_playing == True:
				if track_id != last_id:
					track_name = results['item']['name']
					artist_name = results['item']['artists'][0]['name']
					status_text = "Now Playing: " + track_name + " by " + artist_name
					json_string = '{"status_text":"'+status_text+'","status_emoji":"'+status_emoji+'"}'
					#print json_string
					slack_client.api_call("users.profile.set", profile = json_string)
					last_id = track_id
					time.sleep(poll_interval)
				else:
					time.sleep(poll_interval)
			else: 
				#print "Nothing Playing..."
				last_id = 0
				slack_client.api_call("users.profile.set", profile = clear_status)
				time.sleep(poll_interval)
		else:
			print "Can't get token for", username
			sys.exit()

if __name__ == '__main__':
	sys.exit(main())