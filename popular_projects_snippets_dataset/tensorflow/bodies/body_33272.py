# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_zeros_test.py
operator = linalg_lib.LinearOperatorZeros(num_rows=2)
with self.assertRaisesOpError("non-positive definite"):
    operator.assert_positive_definite()
