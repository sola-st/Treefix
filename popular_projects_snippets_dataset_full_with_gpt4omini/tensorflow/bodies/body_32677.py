# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linalg_ops_test.py
n = 8
for a, b in [[2, -1], [1, 0], [0, 1], [-1e10, 1e10], [-1e-10, 1e-10]]:
    alpha = a * np.ones([n], dtype=dtype)
    beta = b * np.ones([n - 1], dtype=dtype)
    if np.issubdtype(alpha.dtype, np.complexfloating):
        beta += 1j * beta
    self.run_test(alpha, beta)
