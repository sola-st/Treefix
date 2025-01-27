# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_circulant_test.py
with self.cached_session():  # Necessary for fft_kernel_label_map
    # This is a real and hermitian spectrum.
    spectrum = [[1., 2., 2.], [3., 4., 4.], [3., 4., 4.]]
    operator = linalg.LinearOperatorCirculant(spectrum)

    matrix_tensor = operator.to_dense()
    self.assertEqual(matrix_tensor.dtype, dtypes.complex64)
    matrix_t = array_ops.matrix_transpose(matrix_tensor)
    imag_matrix = math_ops.imag(matrix_tensor)
    matrix, matrix_transpose, imag_matrix = self.evaluate(
        [matrix_tensor, matrix_t, imag_matrix])

    np.testing.assert_allclose(0, imag_matrix, atol=1e-6)
    self.assertAllClose(matrix, matrix_transpose, atol=1e-6)
