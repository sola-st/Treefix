# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_test.py
operator = LinearOperatorShape(shape=(2, 3, 4))
self.assertFalse(operator.is_square)
