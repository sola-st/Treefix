# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval.py
# exercise the copy flag in the constructor

# not copying
index = self.create_index(closed=closed)
result = IntervalIndex(index, copy=False)
tm.assert_numpy_array_equal(
    index.left.values, result.left.values, check_same="same"
)
tm.assert_numpy_array_equal(
    index.right.values, result.right.values, check_same="same"
)

# by-definition make a copy
result = IntervalIndex(np.array(index), copy=False)
tm.assert_numpy_array_equal(
    index.left.values, result.left.values, check_same="copy"
)
tm.assert_numpy_array_equal(
    index.right.values, result.right.values, check_same="copy"
)
