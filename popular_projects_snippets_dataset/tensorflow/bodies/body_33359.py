# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_circulant_test.py
with self.cached_session():
    convolution_kernel = [1., 2., 1.]
    spectrum = fft_ops.fft(
        math_ops.cast(convolution_kernel, dtypes.complex64))

    # spectrum is shape [3] ==> operator is shape [3, 3]
    # spectrum is Hermitian ==> operator is real.
    operator = linalg.LinearOperatorCirculant(spectrum)

    # Allow for complex output so we can make sure it has zero imag part.
    self.assertEqual(operator.dtype, dtypes.complex64)

    matrix = self.evaluate(operator.to_dense())
    np.testing.assert_allclose(0, np.imag(matrix), atol=1e-6)
