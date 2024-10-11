# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_test.py
matrix1 = array_ops.placeholder_with_default(
    input=rng.rand(2, 2), shape=None)
operator1 = LinearOperatorMatmulSolve(
    matrix1,
    is_non_singular=False,
    is_self_adjoint=False,
    is_positive_definite=False,
    is_square=True,
)

operator_matmul = operator1.matmul(operator1)

self.assertTrue(operator_matmul.is_square)
self.assertFalse(operator_matmul.is_non_singular)
self.assertEqual(None, operator_matmul.is_self_adjoint)
self.assertEqual(None, operator_matmul.is_positive_definite)

matrix2 = array_ops.placeholder_with_default(
    input=rng.rand(2, 3), shape=None)
operator2 = LinearOperatorMatmulSolve(
    matrix2,
    is_non_singular=False,
    is_self_adjoint=False,
    is_positive_definite=False,
    is_square=False,
)

operator_matmul = operator2.matmul(operator2, adjoint_arg=True)

# Composition recognizes this as the form A @ A.H, which is square, SA.
self.assertTrue(operator_matmul.is_square)
self.assertTrue(operator_matmul.is_self_adjoint)

if context.executing_eagerly():
    # False since we specified is_non_singular=False.
    self.assertFalse(operator_matmul.is_non_singular)
else:
    # May be non-singular, since it's the composition of two non-square.
    # TODO(b/136162840) This is a bit inconsistent, and should probably be
    # False since we specified operator2.is_non_singular == False.
    self.assertIsNone(operator_matmul.is_non_singular)

# No way to deduce these, even in Eager mode.
self.assertIsNone(operator_matmul.is_positive_definite)
