# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/cholesky_op_test.py
data = np.array([[4., -1., 2.], [-1., 6., 0], [2., 0., 5.]])
for dtype in (np.float32, np.float64):
    with self.subTest(dtype=dtype):
        self._verifyCholesky(data.astype(dtype))
for dtype in (np.complex64, np.complex128):
    with self.subTest(dtype=dtype):
        complex_data = np.tril(1j * data, -1).astype(dtype)
        complex_data += np.triu(-1j * data, 1).astype(dtype)
        complex_data += data
        self._verifyCholesky(complex_data)
