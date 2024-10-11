# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/sets_test.py
a_values = [[9, 1, 5], [2, 4, 3]]
b_values = [[1, 9], [1]]
expected_indices = [[0, 0], [0, 1]]
expected_values = _values([1, 9], dtype)
expected_shape = [2, 2]
expected_counts = [2, 0]

# Dense to sparse.
a = _constant(a_values, dtype=dtype)
sp_b = _dense_to_sparse(b_values, dtype=dtype)
intersection = self._set_intersection(a, sp_b)
self._assert_set_operation(
    expected_indices,
    expected_values,
    expected_shape,
    intersection,
    dtype=dtype)
self.assertAllEqual(expected_counts, self._set_intersection_count(a, sp_b))

# Sparse to sparse.
sp_a = _dense_to_sparse(a_values, dtype=dtype)
intersection = self._set_intersection(sp_a, sp_b)
self._assert_set_operation(
    expected_indices,
    expected_values,
    expected_shape,
    intersection,
    dtype=dtype)
self.assertAllEqual(expected_counts,
                    self._set_intersection_count(sp_a, sp_b))
