# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_composition_test.py
matrix = [[11., 0.], [1., 8.]]
x = linalg.LinearOperatorFullMatrix(matrix, is_non_singular=True)
y = linalg.LinearOperatorFullMatrix(matrix, is_non_singular=True)

operator = linalg.LinearOperatorComposition(
    [x, y, y.H, x.H], is_non_singular=None)

self.assertTrue(operator.is_self_adjoint)
self.assertTrue(operator.is_positive_definite)
self.assertTrue(operator.is_non_singular)

with self.assertRaisesRegex(ValueError, "self-adjoint"):
    linalg.LinearOperatorComposition([x, x.H], is_self_adjoint=False)

with self.assertRaisesRegex(ValueError, "non-singular"):
    linalg.LinearOperatorComposition([x, x.H], is_non_singular=False)
