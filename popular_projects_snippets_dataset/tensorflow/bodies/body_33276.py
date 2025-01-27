# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_zeros_test.py
with self.assertRaisesRegex(TypeError, "must be integer"):
    linalg_lib.LinearOperatorZeros(num_rows=2.)
with self.assertRaisesRegex(TypeError, "must be integer"):
    linalg_lib.LinearOperatorZeros(num_rows=2, num_columns=2.)
