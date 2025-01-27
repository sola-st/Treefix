# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_loc.py
# GH#37711
mi = MultiIndex.from_tuples([("a", "A"), ("b", "A")])
obj = DataFrame([1, 2], index=mi)
obj.loc[indexer, :] = 0
expected = DataFrame([0, 2], index=mi)
tm.assert_frame_equal(obj, expected)
