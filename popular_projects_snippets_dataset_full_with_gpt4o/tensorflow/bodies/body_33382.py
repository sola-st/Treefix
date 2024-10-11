# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_circulant_test.py
spectrum = math_ops.cast([[-3j, 4 + 0j], [2j + 2, 3. + 0j]],
                         dtypes.complex64)
operator = linalg.LinearOperatorCirculant2D(spectrum)
with self.cached_session():
    self.evaluate(operator.assert_non_singular())  # Should not fail
