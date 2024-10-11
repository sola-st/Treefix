# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/sets_test.py
a_values = [[1, 1, 1], [1, 5, 9], [4, 5, 3], [5, 5, 1]]
b_values = [[], [1, 2], [1, 2, 2], []]

# a - b.
expected_indices = [[0, 0], [1, 0], [1, 1], [2, 0], [2, 1], [2, 2], [3, 0],
                    [3, 1]]
expected_values = _values([1, 5, 9, 3, 4, 5, 1, 5], dtype)
expected_shape = [4, 3]
expected_counts = [1, 2, 3, 2]

# Dense to sparse.
a = _constant(a_values, dtype=dtype)
sp_b = _dense_to_sparse(b_values, dtype=dtype)
difference = self._set_difference(a, sp_b, True)
self._assert_set_operation(
    expected_indices,
    expected_values,
    expected_shape,
    difference,
    dtype=dtype)
self.assertAllEqual(expected_counts,
                    self._set_difference_count(a, sp_b, True))

# Sparse to sparse.
sp_a = _dense_to_sparse(a_values, dtype=dtype)
difference = self._set_difference(sp_a, sp_b, True)
self._assert_set_operation(
    expected_indices,
    expected_values,
    expected_shape,
    difference,
    dtype=dtype)
self.assertAllEqual(expected_counts,
                    self._set_difference_count(sp_a, sp_b, True))

# b - a.
expected_indices = [[1, 0], [2, 0], [2, 1]]
expected_values = _values([2, 1, 2], dtype)
expected_shape = [4, 2]
expected_counts = [0, 1, 2, 0]

# Dense to sparse.
difference = self._set_difference(a, sp_b, False)
self._assert_set_operation(
    expected_indices,
    expected_values,
    expected_shape,
    difference,
    dtype=dtype)
self.assertAllEqual(expected_counts,
                    self._set_difference_count(a, sp_b, False))

# Sparse to sparse.
difference = self._set_difference(sp_a, sp_b, False)
self._assert_set_operation(
    expected_indices,
    expected_values,
    expected_shape,
    difference,
    dtype=dtype)
self.assertAllEqual(expected_counts,
                    self._set_difference_count(sp_a, sp_b, False))
