# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/lu_op_test.py
data = np.array([[4., -1., 2.], [-1., 6., 0], [10., 0., 5.]])

for dtype in (np.float32, np.float64):
    for output_idx_type in (dtypes.int32, dtypes.int64):
        with self.subTest(dtype=dtype, output_idx_type=output_idx_type):
            self._verifyLu(data.astype(dtype), output_idx_type=output_idx_type)

for dtype in (np.complex64, np.complex128):
    for output_idx_type in (dtypes.int32, dtypes.int64):
        with self.subTest(dtype=dtype, output_idx_type=output_idx_type):
            complex_data = np.tril(1j * data, -1).astype(dtype)
            complex_data += np.triu(-1j * data, 1).astype(dtype)
            complex_data += data
            self._verifyLu(complex_data, output_idx_type=output_idx_type)
