# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linalg_ops_test.py
n = alpha.shape[0]
matrix = np.diag(alpha) + np.diag(beta, 1) + np.diag(np.conj(beta), -1)
# scipy.linalg.eigh_tridiagonal doesn't support complex inputs, so for
# this we call the slower numpy.linalg.eigh.
if np.issubdtype(alpha.dtype, np.complexfloating):
    eigvals_expected, _ = np.linalg.eigh(matrix)
else:
    eigvals_expected = scipy.linalg.eigh_tridiagonal(
        alpha, beta, eigvals_only=True)
eigvals = linalg.eigh_tridiagonal(alpha, beta, eigvals_only=eigvals_only)
if not eigvals_only:
    eigvals, eigvectors = eigvals

eps = np.finfo(alpha.dtype).eps
atol = n * eps * np.amax(np.abs(eigvals_expected))
self.assertAllClose(eigvals_expected, eigvals, atol=atol)
if not eigvals_only:
    self.check_orthogonality(eigvectors, 2 * np.sqrt(n) * eps)
    self.check_residual(matrix, eigvals, eigvectors, atol)
