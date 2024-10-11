# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
# GH#18846
td = Timedelta(hours=3, minutes=4)

assert td // np.nan is NaT
assert np.isnan(td // NaT)
assert np.isnan(td // np.timedelta64("NaT"))
