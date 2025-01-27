# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_circulant_test.py
with self.cached_session() as sess:
    spectrum = math_ops.cast([6., 4, 2], dtypes.complex64)
    operator = linalg.LinearOperatorCirculant(
        spectrum, input_output_dtype=dtypes.complex64)
    matrix, matrix_h = sess.run(
        [operator.to_dense(),
         linalg.adjoint(operator.to_dense())])
    self.assertAllClose(matrix, matrix_h)
    self.evaluate(operator.assert_positive_definite())  # Should not fail
    self.evaluate(operator.assert_self_adjoint())  # Should not fail
