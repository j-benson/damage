import json
import unittest
from unittest.mock import Mock

import message

class TestMessage(unittest.TestCase):

  def setUp(self):
    message.message_file = "messages_test.json"

  def test_within_amount__no_min_max(self):
    self.assertTrue(message.within_amount({ }, 0))
    self.assertTrue(message.within_amount({ }, 1))

    self.assertFalse(message.within_amount({ "amount": { "min": 1 }}, 0))
  def test_within_amount__min(self):
    self.assertTrue(message.within_amount({ "amount": { "min": 0 }}, 0))
    self.assertTrue(message.within_amount({ "amount": { "min": 0 }}, 1))

    self.assertFalse(message.within_amount({ "amount": { "min": 1 }}, 0))
  
  def test_within_amount__max(self):
    self.assertTrue(message.within_amount({ "amount": { "max": 1 }}, 0))
    self.assertTrue(message.within_amount({ "amount": { "max": 1 }}, 1))

    self.assertFalse(message.within_amount({ "amount": { "max": 1 }}, 2))

  def test_within_amount__min_max(self):
    self.assertFalse(message.within_amount({ "amount": { "min": 1, "max": 3 }}, 0))
    self.assertTrue(message.within_amount({ "amount": { "min": 1, "max": 3 }}, 1))
    self.assertTrue(message.within_amount({ "amount": { "min": 1, "max": 3 }}, 2))
    self.assertTrue(message.within_amount({ "amount": { "min": 1, "max": 3 }}, 3))
    self.assertFalse(message.within_amount({ "amount": { "min": 1, "max": 3 }}, 4))
