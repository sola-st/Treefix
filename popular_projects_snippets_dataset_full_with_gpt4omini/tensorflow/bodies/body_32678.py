# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linalg_ops_test.py
for n in [8, 50]:
    alpha = np.random.uniform(size=(n,)).astype(dtype)
    beta = np.random.uniform(size=(n - 1,)).astype(dtype)
    if np.issubdtype(beta.dtype, np.complexfloating):
        beta += 1j * np.random.uniform(size=(n - 1,)).astype(dtype)
    self.run_test(alpha, beta)
