# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tridiagonal_matmul_ops_test.py
self._testAllFormats(
    superdiag=[1], maindiag=[2, 3], subdiag=[4], rhs=[[2, 1], [4, 3]])
