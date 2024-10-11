# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/cholesky_op_test.py
# Verify that LL^T == x.
with self.session() as sess:
    placeholder = array_ops.placeholder(
        dtypes.as_dtype(x.dtype), shape=x.shape)
    with self.test_scope():
        chol = linalg_ops.cholesky(placeholder)
    verification = test_util.matmul_without_tf32(chol, chol, adjoint_b=True)
    self._verifyCholeskyBase(sess, placeholder, x, chol, verification, atol)
