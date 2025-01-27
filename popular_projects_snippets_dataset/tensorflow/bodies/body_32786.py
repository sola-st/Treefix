# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_test.py
with self.assertRaisesRegex(ValueError, "but.*was square"):
    _ = LinearOperatorShape(shape=(2, 4, 4), is_square=False).is_square
