# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_identity_test.py
with self.assertRaisesRegex(ValueError, "must be a 0-D Tensor"):
    linalg_lib.LinearOperatorIdentity(num_rows=[2])
