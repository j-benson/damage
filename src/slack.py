from decimal import Decimal
import re

import slack_api

filter_ifttt_message = lambda m : m["type"] == "message" and "subtype" in m and m["subtype"] == "bot_message" and "username" in m and m["username"] == "IFTTT"
re_amount = re.compile(r"£[\s]*([0-9.]*)")

def sum_spend(fromDate):
  messages = slack_api.get_history(fromDate)
  messages = list(filter(filter_ifttt_message, messages))
  return sum_spend_in_fallback_attachment(messages)

def sum_spend_in_fallback_attachment(messages):
  total_amount = Decimal(0)

  for m in messages:
    if "attachments" in m and len(m["attachments"]) > 0:
      text = m["attachments"][0]["fallback"]
      match = re_amount.search(text)
      if match: 
        total_amount += Decimal(match.group(1))

  return total_amount

