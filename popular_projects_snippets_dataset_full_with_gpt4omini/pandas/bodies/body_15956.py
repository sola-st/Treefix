# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_nunique.py
# GH#18051
ser = Series(Categorical([]))
assert ser.nunique() == 0

ser = Series(Categorical([np.nan]))
assert ser.nunique() == 0
