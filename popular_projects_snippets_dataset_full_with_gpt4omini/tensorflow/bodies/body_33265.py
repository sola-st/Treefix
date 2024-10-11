# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_toeplitz_test.py
with self.assertRaisesRegex(ValueError, "must have at least 1 dimension"):
    linear_operator_toeplitz.LinearOperatorToeplitz(1., 1.)

with self.assertRaisesRegex(ValueError, "must have at least 1 dimension"):
    linear_operator_toeplitz.LinearOperatorToeplitz([1.], 1.)

with self.assertRaisesRegex(ValueError, "must have at least 1 dimension"):
    linear_operator_toeplitz.LinearOperatorToeplitz(1., [1.])
