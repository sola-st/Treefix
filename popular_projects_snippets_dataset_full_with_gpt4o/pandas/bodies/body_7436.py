# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_names.py
# GH#20421
mi = MultiIndex.from_arrays([[1, 2], [3, 4], [5, 6]], names=["x", "y", "x"])
result = getattr(mi, func)(rename_dict)
expected = MultiIndex.from_arrays([[1, 2], [3, 4], [5, 6]], names=exp_names)
tm.assert_index_equal(result, expected)
