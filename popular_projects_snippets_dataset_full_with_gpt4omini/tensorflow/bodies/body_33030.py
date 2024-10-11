# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/cholesky_op_test.py
a = np.random.randn(shape[0], shape[1]).astype(dtype.as_numpy_dtype)
if dtype.is_complex:
    a += 1j * np.random.randn(shape[0], shape[1]).astype(
        dtype.as_numpy_dtype)
exit(a)
