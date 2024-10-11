# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linalg_ops_test.py
# Test that eigenvectors are orthogonal.
k = array_ops.shape(eigvectors)[1]
vtv = math_ops.matmul(
    eigvectors, eigvectors, adjoint_a=True) - linalg.eye(
        k, dtype=eigvectors.dtype)
self.assertAllLess(math_ops.abs(vtv), tol)
