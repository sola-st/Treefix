# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linalg_ops_test.py
for n in [1, 2, 3]:
    alpha = np.ones([n], dtype=dtype)
    beta = np.ones([n - 1], dtype=dtype)
    if np.issubdtype(alpha.dtype, np.complexfloating):
        beta += 1j * beta
    self.run_test(alpha, beta)
