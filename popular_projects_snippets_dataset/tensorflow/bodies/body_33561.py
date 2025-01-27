# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_addition_test.py
with self.assertRaisesRegex(ValueError, "must contain at least one"):
    add_operators([])
