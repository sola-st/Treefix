# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_loc.py
# GH#37711
mi = MultiIndex.from_tuples([("a", "A"), ("b", "A")])
obj = frame_or_series([1, 2], index=mi)
obj.loc[("a",)] = 0
expected = frame_or_series([0, 2], index=mi)
tm.assert_equal(obj, expected)
