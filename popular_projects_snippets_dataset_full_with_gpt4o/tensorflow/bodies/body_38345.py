# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
with self.cached_session():
    self._check([10, 10, 10], [-1], [10, 10, 1])
    self._check([10, 10, 10], [-1, 2], [10, 10, 1])
    self._check([10, 10, 10], [-1, -1], [10, 10, 1])
    self._check([10, 10, 10], [-1, 0], [1, 10, 1])
    self._check([10, 10, 10], [-3], [1, 10, 10])
