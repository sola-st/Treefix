# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
dt_date = datetime(2013, 1, 2)
assert str(dt_date) == str(Timestamp(dt_date))

dt_datetime = datetime(2013, 1, 2, 12, 1, 3)
assert str(dt_datetime) == str(Timestamp(dt_datetime))

dt_datetime_us = datetime(2013, 1, 2, 12, 1, 3, 45)
assert str(dt_datetime_us) == str(Timestamp(dt_datetime_us))

ts_nanos_only = Timestamp(200)
assert str(ts_nanos_only) == "1970-01-01 00:00:00.000000200"

ts_nanos_micros = Timestamp(1200)
assert str(ts_nanos_micros) == "1970-01-01 00:00:00.000001200"
