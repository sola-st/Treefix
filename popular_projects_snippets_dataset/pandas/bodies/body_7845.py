# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_period.py
# #1705
index = date_range("1/1/2012", periods=4, freq="12H")
index_as_arrays = [index.to_period(freq="D"), index.hour]

s = Series([0, 1, 2, 3], index_as_arrays)

assert isinstance(s.index.levels[0], PeriodIndex)

assert isinstance(s.index.values[0][0], Period)
