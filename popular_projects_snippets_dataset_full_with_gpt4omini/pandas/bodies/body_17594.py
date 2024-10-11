# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_custom_business_day.py
assert repr(offset) == "<CustomBusinessDay>"
assert repr(offset2) == "<2 * CustomBusinessDays>"

expected = "<BusinessDay: offset=datetime.timedelta(days=1)>"
assert repr(offset + timedelta(1)) == expected
