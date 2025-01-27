# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_addition_test.py
with self.assertRaisesRegex(TypeError, "contain only LinearOperator"):
    add_operators([1, 2])
