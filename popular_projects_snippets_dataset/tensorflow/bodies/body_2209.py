# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tridiagonal_matmul_ops_test.py
for dtype in [dtypes.float32, dtypes.float64]:
    self._testAllFormats(
        superdiag=[1, 2],
        maindiag=[1, 2, 1],
        subdiag=[2, 1],
        rhs=[[1, 1], [2, 2], [3, 3]],
        dtype=dtype)
