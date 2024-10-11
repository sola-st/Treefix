# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/lu_op_test.py
# This matrix triggers partial pivoting because the first diagonal entry
# is small.
data = np.array([[1e-9, 1., 0.], [1., 0., 0], [0., 1., 5]])
self._verifyLu(data.astype(np.float32))

for dtype in (np.float32, np.float64):
    with self.subTest(dtype=dtype):
        self._verifyLu(data.astype(dtype))
        _, p = linalg_ops.lu(data)
        p_val = self.evaluate([p])
        # Make sure p_val is not the identity permutation.
        self.assertNotAllClose(np.arange(3), p_val)

for dtype in (np.complex64, np.complex128):
    with self.subTest(dtype=dtype):
        complex_data = np.tril(1j * data, -1).astype(dtype)
        complex_data += np.triu(-1j * data, 1).astype(dtype)
        complex_data += data
        self._verifyLu(complex_data)
        _, p = linalg_ops.lu(data)
        p_val = self.evaluate([p])
        # Make sure p_val is not the identity permutation.
        self.assertNotAllClose(np.arange(3), p_val)
