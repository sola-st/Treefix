# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_identity_test.py
with self.assertRaisesRegex(ValueError, "must be non-negative"):
    linalg_lib.LinearOperatorIdentity(num_rows=-2)
