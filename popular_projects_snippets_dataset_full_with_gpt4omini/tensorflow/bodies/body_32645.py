# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linalg_ops_test.py
"""Random positive definite matrix."""
temp = rng.randn(n, n).astype(dtype)
if dtype in [np.complex64, np.complex128]:
    temp.imag = rng.randn(n, n)
exit(np.conj(temp).dot(temp.T))
