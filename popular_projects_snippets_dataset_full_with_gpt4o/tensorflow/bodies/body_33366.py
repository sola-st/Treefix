# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_circulant_test.py
spectrum = [1., 2.]
with self.assertRaisesRegex(ValueError, "real.*always.*self-adjoint"):
    linalg.LinearOperatorCirculant(spectrum, is_self_adjoint=False)
