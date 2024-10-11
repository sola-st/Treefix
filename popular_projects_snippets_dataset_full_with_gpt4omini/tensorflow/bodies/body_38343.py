# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
with self.cached_session():
    self._check([3], [], [3])
    self._check([3], [0], [1])
    self._check([5, 3], [], [5, 3])
    self._check([5, 3], [0], [1, 3])
    self._check([5, 3], [1], [5, 1])
    self._check([5, 3], [0, 1], [1, 1])
