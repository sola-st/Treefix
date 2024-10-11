# Extracted from ./data/repos/pandas/pandas/tests/series/test_api.py
ser = Series({"year": 2000, "month": 1, "day": 10})
msg = "'Series' object has no attribute 'weekday'"
with pytest.raises(AttributeError, match=msg):
    ser.weekday
