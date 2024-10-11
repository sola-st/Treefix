# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linalg_ops_test.py
# Test that A*eigvectors is close to eigvectors*diag(eigvals).
l = math_ops.cast(linalg.diag(eigvals), dtype=eigvectors.dtype)
av = math_ops.matmul(matrix, eigvectors)
vl = math_ops.matmul(eigvectors, l)
self.assertAllClose(av, vl, atol=atol)
