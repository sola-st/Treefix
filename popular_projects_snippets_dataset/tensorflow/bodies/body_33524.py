# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_identity_test.py
# Many "test_...num_rows" tests are performed in LinearOperatorIdentity.
with self.assertRaisesRegex(ValueError, "must be a 0-D Tensor"):
    linalg_lib.LinearOperatorScaledIdentity(
        num_rows=[2], multiplier=123.)
