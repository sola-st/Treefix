# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/sets_test.py
self.assertAllEqual([1], self._set_size(_dense_to_sparse([[1]], dtype)))
self.assertAllEqual([2, 1],
                    self._set_size(_dense_to_sparse([[1, 9], [1]], dtype)))
self.assertAllEqual(
    [3, 0], self._set_size(_dense_to_sparse([[1, 9, 2], []], dtype)))
self.assertAllEqual(
    [0, 3], self._set_size(_dense_to_sparse([[], [1, 9, 2]], dtype)))
