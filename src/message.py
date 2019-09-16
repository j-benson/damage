import json
import random

message_file = "messages.json"
base_message = "Last night's damage was £{}."

def create_message(amount=0, day=None):
  messages = load_messages()
  messages = filter_messages(messages, amount=amount, day=day)
  message = select_message(messages)
  return message.format(amount)
  
def load_messages():
  with open(message_file) as data:
    return json.load(data)

def filter_messages(messages, amount, day):
  return list(filter(lambda m: within_amount(m, amount), messages))

def within_amount(message, amount):
  min = 0
  max = 100000
  if "amount" in message:
    if "min" in message["amount"]:
      min = message["amount"]["min"]
    if "max" in message["amount"]:
      max = message["amount"]["max"]

  return amount >= min and amount <= max

def select_message(messages):
  if len(messages) == 0:
    return base_message
  else:
    i = random.randint(0, len(messages) - 1)
    return "{} {}".format(base_message, messages[i]["message"])
