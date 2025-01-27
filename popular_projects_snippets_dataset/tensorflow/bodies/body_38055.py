# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/sets_test.py
self.assertAllEqual(
    [1], self._set_size(_dense_to_sparse([[1, 1, 1, 1, 1, 1]], dtype)))
self.assertAllEqual([2, 7, 3, 0, 1],
                    self._set_size(
                        _dense_to_sparse([[1, 9], [
                            6, 7, 8, 8, 6, 7, 5, 3, 3, 0, 6, 6, 9, 0, 0, 0
                        ], [999, 1, -1000], [], [-1]], dtype)))
