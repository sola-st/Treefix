# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
for dtype in [
    np.int32, np.float32, np.float64, np.complex64, np.complex128
]:
    for degree in range(5):
        with self.subTest(dtype=dtype, degree=degree):
            self._runtest(dtype, degree)
