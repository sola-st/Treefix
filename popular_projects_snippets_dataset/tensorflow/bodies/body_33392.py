# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_circulant_test.py
with self.cached_session():  # Necessary for fft_kernel_label_map
    # S is real and positive.
    s = linear_operator_test_util.random_uniform(
        shape=(10, 2, 3, 4), dtype=dtypes.float32, minval=1., maxval=2.)

    # Let S = S1 + S2, the Hermitian and anti-hermitian parts.
    # S1 = 0.5 * (S + S^H), S2 = 0.5 * (S - S^H),
    # where ^H is the Hermitian transpose of the function:
    #    f(n0, n1, n2)^H := ComplexConjugate[f(N0-n0, N1-n1, N2-n2)].
    # We want to isolate S1, since
    #   S1 is Hermitian by construction
    #   S1 is real since S is
    #   S1 is positive since it is the sum of two positive kernels

    # IDFT[S] = IDFT[S1] + IDFT[S2]
    #         =      H1  +      H2
    # where H1 is real since it is Hermitian,
    # and H2 is imaginary since it is anti-Hermitian.
    ifft_s = fft_ops.ifft3d(math_ops.cast(s, dtypes.complex64))

    # Throw away H2, keep H1.
    real_ifft_s = math_ops.real(ifft_s)

    # This is the perfect spectrum!
    # spectrum = DFT[H1]
    #          = S1,
    fft_real_ifft_s = fft_ops.fft3d(
        math_ops.cast(real_ifft_s, dtypes.complex64))

    # S1 is Hermitian ==> operator is real.
    # S1 is real ==> operator is self-adjoint.
    # S1 is positive ==> operator is positive-definite.
    operator = linalg.LinearOperatorCirculant3D(fft_real_ifft_s)

    # Allow for complex output so we can check operator has zero imag part.
    self.assertEqual(operator.dtype, dtypes.complex64)
    matrix, matrix_t = self.evaluate([
        operator.to_dense(),
        array_ops.matrix_transpose(operator.to_dense())
    ])
    self.evaluate(operator.assert_positive_definite())  # Should not fail.
    np.testing.assert_allclose(0, np.imag(matrix), atol=1e-6)
    self.assertAllClose(matrix, matrix_t)

    # Just to test the theory, get S2 as well.
    # This should create an imaginary operator.
    # S2 is anti-Hermitian ==> operator is imaginary.
    # S2 is real ==> operator is self-adjoint.
    imag_ifft_s = math_ops.imag(ifft_s)
    fft_imag_ifft_s = fft_ops.fft3d(
        1j * math_ops.cast(imag_ifft_s, dtypes.complex64))
    operator_imag = linalg.LinearOperatorCirculant3D(fft_imag_ifft_s)

    matrix, matrix_h = self.evaluate([
        operator_imag.to_dense(),
        array_ops.matrix_transpose(math_ops.conj(operator_imag.to_dense()))
    ])
    self.assertAllClose(matrix, matrix_h)
    np.testing.assert_allclose(0, np.real(matrix), atol=1e-7)
