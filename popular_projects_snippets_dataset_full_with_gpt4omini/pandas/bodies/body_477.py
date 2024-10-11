# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py

dr1 = date_range("2013-01-01", periods=3, tz="US/Eastern")
s1 = Series(dr1, name="A")
assert is_datetime64tz_dtype(s1)

dr2 = date_range("2013-08-01", periods=3, tz="US/Eastern")
s2 = Series(dr2, name="A")
assert is_datetime64tz_dtype(s2)
assert s1.dtype == s2.dtype
