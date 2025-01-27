# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
# GH#8142
delta = dtype(delta)
index = Index([10, 11, 12], dtype=dtype)
result = index + delta
expected = Index(index.values + delta, dtype=dtype)
tm.assert_index_equal(result, expected)

# this subtraction used to fail
result = index - delta
expected = Index(index.values - delta, dtype=dtype)
tm.assert_index_equal(result, expected)

tm.assert_index_equal(index + index, 2 * index)
tm.assert_index_equal(index - index, 0 * index)
assert not (index - index).empty
