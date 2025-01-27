# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_identity_test.py
with self.assertRaisesRegex(TypeError, "num_rows.*reference"):
    linalg_lib.LinearOperatorIdentity(num_rows=variables_module.Variable(2))

with self.assertRaisesRegex(TypeError, "batch_shape.*reference"):
    linalg_lib.LinearOperatorIdentity(
        num_rows=2, batch_shape=variables_module.Variable([3]))
