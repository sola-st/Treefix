# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
freq = to_offset("B")

ts = Timestamp("2017-10-01")
assert ts.dayofweek == 6
assert ts.day_of_week == 6
assert ts.is_month_start  # not a weekday
assert not freq.is_month_start(ts)
assert freq.is_month_start(ts + Timedelta(days=1))
assert not freq.is_quarter_start(ts)
assert freq.is_quarter_start(ts + Timedelta(days=1))

ts = Timestamp("2017-09-30")
assert ts.dayofweek == 5
assert ts.day_of_week == 5
assert ts.is_month_end
assert not freq.is_month_end(ts)
assert freq.is_month_end(ts - Timedelta(days=1))
assert ts.is_quarter_end
assert not freq.is_quarter_end(ts)
assert freq.is_quarter_end(ts - Timedelta(days=1))
