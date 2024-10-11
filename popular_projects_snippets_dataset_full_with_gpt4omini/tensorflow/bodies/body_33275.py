# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_zeros_test.py
with self.assertRaisesRegex(ValueError, "must be a 0-D Tensor"):
    linalg_lib.LinearOperatorZeros(num_rows=[2])
with self.assertRaisesRegex(ValueError, "must be a 0-D Tensor"):
    linalg_lib.LinearOperatorZeros(num_rows=2, num_columns=[2])
