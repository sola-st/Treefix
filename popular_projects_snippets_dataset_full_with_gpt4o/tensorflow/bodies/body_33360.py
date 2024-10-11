# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_circulant_test.py
with self.cached_session():
    # Make spectrum the FFT of a real convolution kernel h.  This ensures that
    # spectrum is Hermitian.
    h = linear_operator_test_util.random_normal(shape=(3, 4))
    spectrum = fft_ops.fft(math_ops.cast(h, dtypes.complex64))
    operator = linalg.LinearOperatorCirculant(
        spectrum, input_output_dtype=dtypes.complex64)
    matrix = operator.to_dense()
    imag_matrix = math_ops.imag(matrix)
    eps = np.finfo(np.float32).eps
    np.testing.assert_allclose(
        0, self.evaluate(imag_matrix), rtol=0, atol=eps * 3 * 4)
