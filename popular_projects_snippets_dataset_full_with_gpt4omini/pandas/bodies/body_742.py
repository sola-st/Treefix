# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
assert is_scalar(Timestamp("2014-01-01"))
assert is_scalar(Timedelta(hours=1))
assert is_scalar(Period("2014-01-01"))
assert is_scalar(Interval(left=0, right=1))
assert is_scalar(DateOffset(days=1))
assert is_scalar(pd.offsets.Minute(3))
