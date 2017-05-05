import os
import auth_keys
from slackclient import SlackClient

slack_client = SlackClient(auth_keys.SLACK_BOT_TOKEN)

status_text = "song 3"
status_emoji = ":musical_note:"

json_string = "{'status_text':'"+status_text+"','status_emoji':'"+status_emoji+"'}"

if __name__ == "__main__":
    slack_client.api_call("users.profile.set", profile = json_string)

