# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_circulant_test.py
spectrum = math_ops.cast([6. + 0j, 4 + 0j, 2j + 2], dtypes.complex64)
operator = linalg.LinearOperatorCirculant(spectrum)
with self.cached_session():
    self.evaluate(operator.assert_positive_definite())  # Should not fail
