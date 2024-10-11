# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/sets_test.py
a_values = [[9, 1, 5], [2, 4, 3]]
b_values = [[1, 9], [1, 2]]
expected_indices = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [1, 3]]
expected_values = _values([1, 5, 9, 1, 2, 3, 4], dtype)
expected_shape = [2, 4]
expected_counts = [3, 4]

# Dense to dense.
a = _constant(a_values, dtype=dtype)
b = _constant(b_values, dtype=dtype)
union = self._set_union(a, b)
self._assert_set_operation(
    expected_indices, expected_values, expected_shape, union, dtype=dtype)
self.assertAllEqual(expected_counts, self._set_union_count(a, b))
