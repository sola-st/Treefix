# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/cholesky_op_test.py
n = 2000
shape = (n, n)
data = np.ones(shape).astype(np.float32) / (2.0 * n) + np.diag(
    np.ones(n).astype(np.float32))
self._verifyCholesky(data, atol=1e-4)
