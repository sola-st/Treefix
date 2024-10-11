# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_business_day.py
assert repr(offset) == "<BusinessDay>"
assert repr(offset2) == "<2 * BusinessDays>"

expected = "<BusinessDay: offset=datetime.timedelta(days=1)>"
assert repr(offset + timedelta(1)) == expected
