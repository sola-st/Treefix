# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_kronecker_test.py
with self.assertRaisesRegex(ValueError, ">=1 operators"):
    kronecker.LinearOperatorKronecker([])
