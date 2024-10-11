# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/sets_test.py
sp_a = _dense_to_sparse(
    [[], [1, 5, 9], [4, 5, 3, 3, 4, 5], [5, 1]], dtype=dtype)
sp_b = _dense_to_sparse([[], [1, 2], [1, 2, 2], []], dtype=dtype)

# a - b.
expected_indices = [[1, 0], [1, 1], [2, 0], [2, 1], [2, 2], [3, 0], [3, 1]]
expected_values = _values([5, 9, 3, 4, 5, 1, 5], dtype)
expected_shape = [4, 3]
expected_counts = [0, 2, 3, 2]

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

difference = self._set_difference(sp_a, sp_b, False)
self._assert_set_operation(
    expected_indices,
    expected_values,
    expected_shape,
    difference,
    dtype=dtype)
self.assertAllEqual(expected_counts,
                    self._set_difference_count(sp_a, sp_b, False))
