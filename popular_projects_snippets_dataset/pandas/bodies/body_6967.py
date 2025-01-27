# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_setops.py
# GH#36289
dtype = any_numpy_dtype_for_small_pos_integer_indexes
a = Index([1, 0, 0], dtype=dtype)
b = Index([0, 1], dtype=dtype)
expected = Index([0, 0, 1], dtype=dtype)

result = a.union(b)
tm.assert_index_equal(result, expected)

result = b.union(a)
tm.assert_index_equal(result, expected)
