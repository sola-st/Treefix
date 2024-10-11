# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_zeros_test.py
with self.assertRaisesOpError("non-invertible"):
    operator = linalg_lib.LinearOperatorZeros(num_rows=2)
    operator.assert_non_singular()
