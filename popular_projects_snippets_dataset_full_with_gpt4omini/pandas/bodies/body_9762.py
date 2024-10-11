# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling_skew_kurt.py
# #18804 all rolling kurt for all equal values should return Nan
# #46717 update: all equal values should return -3 instead of NaN
a = Series([1.1] * 15).rolling(window=10, step=step).kurt()
assert (a[a.index >= 9] == -3).all()
assert a[a.index < 9].isna().all()
