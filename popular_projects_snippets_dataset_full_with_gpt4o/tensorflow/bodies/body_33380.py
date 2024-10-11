# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_circulant_test.py
with self.cached_session():
    # This is a real and hermitian spectrum.
    spectrum = linear_operator_test_util.random_normal(
        shape=(3, 3), dtype=dtypes.float32)
    operator = linalg.LinearOperatorCirculant2D(spectrum)

    matrix_tensor = operator.to_dense()
    self.assertEqual(matrix_tensor.dtype, dtypes.complex64)
    matrix_h = linalg.adjoint(matrix_tensor)
    matrix, matrix_h = self.evaluate([matrix_tensor, matrix_h])
    self.assertAllClose(matrix, matrix_h, atol=1e-5)
