# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
series = Series(date_range("1/1/2000", periods=10))
series[3] = None
assert series[3] is NaT

series[3:5] = None
assert series[4] is NaT

series[5] = np.nan
assert series[5] is NaT

series[5:7] = np.nan
assert series[6] is NaT
