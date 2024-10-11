# Extracted from ./data/repos/pandas/pandas/tests/series/test_api.py
# attribute access should still work!
ser = Series({"year": 2000, "month": 1, "day": 10})
assert ser.year == 2000
assert ser.month == 1
assert ser.day == 10
