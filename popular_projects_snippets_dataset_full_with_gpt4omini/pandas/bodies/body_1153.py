# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_loc.py
# GH#43908
mi = MultiIndex.from_tuples([(1, 2), (3, (4, 5))])
ser = Series([1, 2], index=mi)
result = ser.loc[(3, (4, 5))]
assert result == 2
