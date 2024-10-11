# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_range.py
# GH#41151
values = RangeIndex(0, 1)
result = base.isin(values)
expected = np.array([True, False])
tm.assert_numpy_array_equal(result, expected)
