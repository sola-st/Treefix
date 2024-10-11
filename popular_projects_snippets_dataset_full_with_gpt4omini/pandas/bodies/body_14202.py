# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
utc = dateutil.tz.tzutc()

dt_date = datetime(2013, 1, 2, tzinfo=utc)
assert str(dt_date) == str(Timestamp(dt_date))

dt_datetime = datetime(2013, 1, 2, 12, 1, 3, tzinfo=utc)
assert str(dt_datetime) == str(Timestamp(dt_datetime))

dt_datetime_us = datetime(2013, 1, 2, 12, 1, 3, 45, tzinfo=utc)
assert str(dt_datetime_us) == str(Timestamp(dt_datetime_us))
