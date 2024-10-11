# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_searchsorted.py
# GH 30086
ser = Series(date_range("20120101", periods=10, freq="2D", tz="UTC"))
val = Timestamp("20120102", tz="America/New_York")
res = ser.searchsorted(val)
assert is_scalar(res)
assert res == 1
