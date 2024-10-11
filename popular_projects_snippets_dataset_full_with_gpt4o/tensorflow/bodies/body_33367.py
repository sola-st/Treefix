# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_circulant_test.py
spectrum = [1., 2.]
operator = linalg.LinearOperatorCirculant(spectrum)
self.assertTrue(operator.is_self_adjoint)
