# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_setops.py
# GH#31326
dtype = any_numpy_dtype_for_small_pos_integer_indexes
a = Index([1, 2, 2, 3], dtype=dtype)
b = Index([3, 3, 4], dtype=dtype)

expected = Index([1, 2, 2, 3, 3, 4], dtype=dtype)
if isinstance(a, CategoricalIndex):
    expected = Index([1, 2, 2, 3, 3, 4])
result = a.union(b)
tm.assert_index_equal(result, expected)
result = a.union(b, sort=False)
tm.assert_index_equal(result, expected)
