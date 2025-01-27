# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/cholesky_op_test.py
# Verify that LL^T == x.
chol = linalg_ops.cholesky(x)
verification = test_util.matmul_without_tf32(chol, chol, adjoint_b=True)
self._verifyCholeskyBase(x, chol, verification)
