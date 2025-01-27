# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_full_matrix_test.py
with self.assertRaisesRegex(ValueError, "at least 2 dimensions"):
    linalg.LinearOperatorFullMatrix([1.])
