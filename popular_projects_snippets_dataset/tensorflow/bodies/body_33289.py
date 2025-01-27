# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_zeros_test.py
with self.assertRaisesRegex(TypeError, "num_rows.cannot.be.reference"):
    linalg_lib.LinearOperatorZeros(num_rows=variables_module.Variable(2))

with self.assertRaisesRegex(TypeError, "num_columns.cannot.be.reference"):
    linalg_lib.LinearOperatorZeros(
        num_rows=2, num_columns=variables_module.Variable(3))

with self.assertRaisesRegex(TypeError, "batch_shape.cannot.be.reference"):
    linalg_lib.LinearOperatorZeros(
        num_rows=2, batch_shape=variables_module.Variable([2]))
