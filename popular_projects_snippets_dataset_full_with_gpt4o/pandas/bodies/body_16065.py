# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_searchsorted.py
ser = Series(date_range("20120101", periods=10, freq="2D"))
val = Timestamp("20120102")
res = ser.searchsorted(val)
assert is_scalar(res)
assert res == 1
