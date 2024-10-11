# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_householder_test.py
with self.assertRaisesRegex(ValueError, "must have at least 1 dimension"):
    householder.LinearOperatorHouseholder(1.)
