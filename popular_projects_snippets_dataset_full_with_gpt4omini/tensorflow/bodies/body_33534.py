# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_identity_test.py
with self.assertRaisesRegex(TypeError, "num_rows.*reference"):
    linalg_lib.LinearOperatorScaledIdentity(
        num_rows=variables_module.Variable(2), multiplier=1.23)
