# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/sets_test.py
a_values = [[1, 1, 3]]
b_values = [[1]]
expected_indices = [[0, 0], [0, 1]]
expected_values = _values([1, 3], dtype)
expected_shape = [1, 2]

# Dense to sparse.
a = _constant(a_values, dtype=dtype)
sp_b = _dense_to_sparse(b_values, dtype=dtype)
union = self._set_union(a, sp_b)
self._assert_set_operation(
    expected_indices, expected_values, expected_shape, union, dtype=dtype)
self.assertAllEqual([2], self._set_union_count(a, sp_b))

# Sparse to sparse.
sp_a = _dense_to_sparse(a_values, dtype=dtype)
union = self._set_union(sp_a, sp_b)
self._assert_set_operation(
    expected_indices, expected_values, expected_shape, union, dtype=dtype)
self.assertAllEqual([2], self._set_union_count(sp_a, sp_b))
