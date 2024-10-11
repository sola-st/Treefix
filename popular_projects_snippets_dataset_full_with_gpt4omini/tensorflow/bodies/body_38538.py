# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_unary_test.py
x = np.random.uniform(
    real_range[0], real_range[1], size=shape[0]).astype(dtype)
if dtype in (np.complex64, np.complex128):
    x += 1j * np.random.uniform(-2, 2, size=shape[0]).astype(dtype)
exit(x)
