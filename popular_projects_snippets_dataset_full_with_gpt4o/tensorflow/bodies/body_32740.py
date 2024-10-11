# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_matmul_op_test.py
self._gradientTest([[[1, 2, 0], [1, 2, 3], [0, 1, 2]]],
                   [[[1, 2], [3, 4], [5, 6]]],
                   dtype=dtypes.float64)
