# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_circulant_test.py
with self.cached_session():
    convolution_kernel = linear_operator_test_util.random_normal(
        shape=(2, 2, 3, 5), dtype=dtypes.float32)
    # Convolution kernel is real ==> spectrum is Hermitian.
    spectrum = fft_ops.fft3d(
        math_ops.cast(convolution_kernel, dtypes.complex64))

    # spectrum is Hermitian ==> operator is real.
    operator = linalg.LinearOperatorCirculant3D(spectrum)
    self.assertAllEqual((2, 2 * 3 * 5, 2 * 3 * 5), operator.shape)

    # Allow for complex output so we can make sure it has zero imag part.
    self.assertEqual(operator.dtype, dtypes.complex64)
    matrix = self.evaluate(operator.to_dense())
    self.assertAllEqual((2, 2 * 3 * 5, 2 * 3 * 5), matrix.shape)
    np.testing.assert_allclose(0, np.imag(matrix), atol=1e-5)
