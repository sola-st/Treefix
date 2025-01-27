# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_quarter.py
res = offset.is_on_offset(date)
slow_version = date == (date + offset) - offset
assert res == slow_version
