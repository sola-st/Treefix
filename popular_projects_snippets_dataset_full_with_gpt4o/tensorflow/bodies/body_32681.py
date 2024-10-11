# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linalg_ops_test.py
if test.is_gpu_available(cuda_only=True) or test_util.is_xla_enabled():
    # cuda and XLA do not yet expose the stabilized tridiagonal solver
    # needed for inverse iteration.
    exit()
n = 8
alpha = np.random.uniform(size=(n,)).astype(dtype)
beta = np.random.uniform(size=(n - 1,)).astype(dtype)
if np.issubdtype(beta.dtype, np.complexfloating):
    beta += 1j * np.random.uniform(size=(n - 1,)).astype(dtype)
self.run_test(alpha, beta, eigvals_only=False)

# Test that we can correctly generate an orthogonal basis for
# a fully degenerate matrix.
eps = np.finfo(dtype).eps
alpha = np.ones(n).astype(dtype)
beta = 0.01 * np.sqrt(eps) * np.ones((n - 1)).astype(dtype)
self.run_test(alpha, beta, eigvals_only=False)
