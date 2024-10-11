# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_zeros_test.py
operator1 = linalg_lib.LinearOperatorIdentity(num_rows=2)
operator2 = linalg_lib.LinearOperatorZeros(num_rows=2)
self.assertTrue(isinstance(
    operator1.matmul(operator2),
    linalg_lib.LinearOperatorZeros))

self.assertTrue(isinstance(
    operator2.matmul(operator1),
    linalg_lib.LinearOperatorZeros))
