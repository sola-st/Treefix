# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_matmul_op_test.py
for dtype in [dtypes.float32, dtypes.float64]:
    self._testAllFormats([1, 2], [1, 2, 1], [2, 1], [[1, 1], [2, 2], [3, 3]],
                         [[3, 3], [12, 12], [5, 5]],
                         dtype=dtype)
