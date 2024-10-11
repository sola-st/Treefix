# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tridiagonal_matmul_ops_test.py
self._gradientTest([[[1, 2, 0], [1, 2, 3], [0, 1, 2]]],
                   [[[1, 2], [3, 4], [5, 6]]],
                   dtype=dtypes.float64)
