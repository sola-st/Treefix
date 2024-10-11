# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_zeros_test.py
with self.assertRaisesRegex(ValueError, "must be a 1-D"):
    linalg_lib.LinearOperatorZeros(num_rows=2, batch_shape=2)
