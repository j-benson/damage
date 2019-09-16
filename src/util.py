from datetime import date, datetime, timedelta

def yesterday():
  y = date.today() - timedelta(days=1)
  return datetime(y.year, y.month, y.day)