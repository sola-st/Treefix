# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
"""Check that reduced_shape does the right thing with zero dimensions."""
with self.cached_session():
    self._check([0], [], [0])
    self._check([0], [0], [1])
    self._check([0, 3], [], [0, 3])
    self._check([0, 3], [0], [1, 3])
    self._check([0, 3], [1], [0, 1])
    self._check([0, 3], [0, 1], [1, 1])
    self._check([3, 0], [], [3, 0])
    self._check([3, 0], [0], [1, 0])
    self._check([3, 0], [1], [3, 1])
    self._check([3, 0], [0, 1], [1, 1])
