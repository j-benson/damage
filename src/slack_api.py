import os
import json
import urllib.request
import re

channel_id = os.environ["DAMAGE_SLACK_CHANNEL"]
oauthToken = os.environ["DAMAGE_SLACK_OAUTH"]
webhook_url = os.environ["DAMAGE_SLACK_WEBHOOK"]

def post_message(message):
  headers = { "Content-Type" : "application/json" }
  payload = { "text" : message }
  request = urllib.request.Request(method="POST", url=webhook_url, headers=headers, data=bytes(json.dumps(payload), 'utf-8'))
  with urllib.request.urlopen(request) as f:
    pass

def get_history(fromDate):
  with urllib.request.urlopen("https://slack.com/api/channels.history?channel={}&oldest={}&token={}".format(channel_id, fromDate.timestamp(), oauthToken)) as response:
    res_json = json.loads(response.read())

  if not res_json["ok"]:
    print(res_json)
    raise Exception("Response not ok")

  return res_json["messages"]