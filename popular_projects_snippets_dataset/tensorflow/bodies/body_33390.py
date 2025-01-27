# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_circulant_test.py
with self.cached_session():
    # This is a real and hermitian spectrum.
    spectrum = linear_operator_test_util.random_normal(
        shape=(2, 2, 3, 5), dtype=dtypes.float32)
    operator = linalg.LinearOperatorCirculant3D(spectrum)
    self.assertAllEqual((2, 2 * 3 * 5, 2 * 3 * 5), operator.shape)

    self.assertEqual(
        operator.parameters,
        {
            "input_output_dtype": dtypes.complex64,
            "is_non_singular": None,
            "is_positive_definite": None,
            "is_self_adjoint": None,
            "is_square": True,
            "name": "LinearOperatorCirculant3D",
            "spectrum": spectrum,
        })

    matrix_tensor = operator.to_dense()
    self.assertEqual(matrix_tensor.dtype, dtypes.complex64)
    matrix_h = linalg.adjoint(matrix_tensor)

    matrix, matrix_h = self.evaluate([matrix_tensor, matrix_h])
    self.assertAllEqual((2, 2 * 3 * 5, 2 * 3 * 5), matrix.shape)
    self.assertAllClose(matrix, matrix_h)
