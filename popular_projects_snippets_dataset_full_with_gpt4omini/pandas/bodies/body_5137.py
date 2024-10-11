# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
# GH#18846
td = Timedelta(hours=3, minutes=3)

assert np.isnan(td.__rfloordiv__(NaT))
assert np.isnan(td.__rfloordiv__(np.timedelta64("NaT")))
