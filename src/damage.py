import message
import slack
import slack_api
import util

def main():
  try:
    spend = slack.sum_spend(util.yesterday())
    if spend > 0:
      damage_message = message.create_message(spend)
      slack_api.post_message(damage_message)
  except Exception as e:
    print(e)
    raise e