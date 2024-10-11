# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_business_day.py
offset = offset + timedelta(hours=2)

assert (dt + offset) == datetime(2008, 1, 2, 2)
