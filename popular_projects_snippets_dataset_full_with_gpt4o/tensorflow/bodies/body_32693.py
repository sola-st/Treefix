# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_diag_test.py
with self.assertRaisesRegex(ValueError, "must have at least 1 dimension"):
    linalg.LinearOperatorDiag(1.)
