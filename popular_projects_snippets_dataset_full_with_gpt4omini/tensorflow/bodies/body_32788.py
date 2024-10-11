# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_test.py
operator = LinearOperatorShape((2, 3))
with self.assertRaisesRegex(NotImplementedError, "not be square"):
    operator.determinant()
with self.assertRaisesRegex(NotImplementedError, "not be square"):
    operator.log_abs_determinant()
with self.assertRaisesRegex(NotImplementedError, "not be square"):
    operator.solve(rng.rand(2, 2))

with self.assertRaisesRegex(ValueError, "is always square"):
    matrix = array_ops.placeholder_with_default(input=(), shape=None)
    LinearOperatorMatmulSolve(
        matrix, is_positive_definite=True, is_square=False)
