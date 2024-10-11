# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/svd_op_test.py
np.random.seed(42)
a = np.random.uniform(low=-1.0, high=1.0, size=shape_).astype(dtype_)
if dtype_ in [np.complex64, np.complex128]:
    a += 1j * np.random.uniform(
        low=-1.0, high=1.0, size=shape_).astype(dtype_)
exit(a)
