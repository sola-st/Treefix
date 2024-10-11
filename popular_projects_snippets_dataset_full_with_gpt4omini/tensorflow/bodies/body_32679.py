# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linalg_ops_test.py
n = 4
alpha = np.random.uniform(size=(n,)).astype(dtype)
beta = np.random.uniform(size=(n - 1,)).astype(dtype)
eigvals_all = linalg.eigh_tridiagonal(alpha, beta, select="a")

eps = np.finfo(alpha.dtype).eps
atol = 2 * n * eps
for first in range(n - 1):
    for last in range(first + 1, n - 1):
        # Check that we get the expected eigenvalues by selecting by
        # index range.
        eigvals_index = linalg.eigh_tridiagonal(
            alpha, beta, select="i", select_range=(first, last))
        self.assertAllClose(
            eigvals_all[first:(last + 1)], eigvals_index, atol=atol)

        # Check that we get the expected eigenvalues by selecting by
        # value range.
        eigvals_value = linalg.eigh_tridiagonal(
            alpha,
            beta,
            select="v",
            select_range=(eigvals_all[first], eigvals_all[last]))
        self.assertAllClose(
            eigvals_all[first:(last + 1)], eigvals_value, atol=atol)
