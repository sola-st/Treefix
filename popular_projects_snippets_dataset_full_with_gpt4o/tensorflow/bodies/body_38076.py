# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/sets_test.py
a_values = [[1, 5, 9], [4, 5, 3]]
b_values = [[1, 2, 6], [1, 2, 2]]

# a - b.
expected_indices = [[0, 0], [0, 1], [1, 0], [1, 1], [1, 2]]
expected_values = _values([5, 9, 3, 4, 5], dtype)
expected_shape = [2, 3]
expected_counts = [2, 3]

# Dense to dense.
a = _constant(a_values, dtype=dtype)
b = _constant(b_values, dtype=dtype)
difference = self._set_difference(a, b, True)
self._assert_set_operation(
    expected_indices,
    expected_values,
    expected_shape,
    difference,
    dtype=dtype)
self.assertAllEqual(expected_counts, self._set_difference_count(a, b, True))

# b - a.
expected_indices = [[0, 0], [0, 1], [1, 0], [1, 1]]
expected_values = _values([2, 6, 1, 2], dtype)
expected_shape = [2, 2]
expected_counts = [2, 2]

# Dense to dense.
difference = self._set_difference(a, b, False)
self._assert_set_operation(
    expected_indices,
    expected_values,
    expected_shape,
    difference,
    dtype=dtype)
self.assertAllEqual(expected_counts,
                    self._set_difference_count(a, b, False))
