import datetime as dt

anmeldetag = dt.datetime(year=2024, month=10, day=28)
print("Späteste Abgabe am", anmeldetag+dt.timedelta(days=9*7))
