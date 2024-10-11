# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_identity_test.py
with self.assertRaisesRegex(TypeError, "must be integer"):
    linalg_lib.LinearOperatorIdentity(num_rows=2.)
