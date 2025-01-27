# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_test.py
matrix = array_ops.placeholder_with_default(input=np.ones((2, 2)),
                                            shape=None)
operator1 = LinearOperatorMatmulSolve(matrix)

operator_matmul = operator1.matmul(operator1)

if not context.executing_eagerly():
    # Eager mode will read in the input and discover matrix is square.
    self.assertEqual(None, operator_matmul.is_square)
self.assertEqual(None, operator_matmul.is_non_singular)
self.assertEqual(None, operator_matmul.is_self_adjoint)
self.assertEqual(None, operator_matmul.is_positive_definite)

operator2 = LinearOperatorMatmulSolve(
    matrix,
    is_non_singular=True,
    is_self_adjoint=True,
    is_positive_definite=True,
    is_square=True,
)

operator_matmul = operator2.matmul(operator2)

self.assertTrue(operator_matmul.is_square)
self.assertTrue(operator_matmul.is_non_singular)

# A @ A is SA since A is.
self.assertEqual(True, operator_matmul.is_self_adjoint)

# A @ A is non-singular (since A is) and A @ A = A @ A.H is semi-def so...
self.assertEqual(True, operator_matmul.is_positive_definite)
