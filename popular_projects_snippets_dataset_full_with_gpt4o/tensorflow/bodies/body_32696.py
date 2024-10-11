# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_diag_test.py
operator1 = linalg_lib.LinearOperatorDiag([2., 3.], is_non_singular=True)
operator2 = linalg_lib.LinearOperatorDiag([1., 2.], is_non_singular=True)
operator3 = linalg_lib.LinearOperatorScaledIdentity(
    num_rows=2, multiplier=3., is_non_singular=True)
operator_solve = operator1.solve(operator2)
self.assertTrue(isinstance(
    operator_solve,
    linalg_lib.LinearOperatorDiag))
self.assertAllClose([0.5, 2 / 3.], self.evaluate(operator_solve.diag))

operator_solve = operator2.solve(operator1)
self.assertTrue(isinstance(
    operator_solve,
    linalg_lib.LinearOperatorDiag))
self.assertAllClose([2., 3 / 2.], self.evaluate(operator_solve.diag))

operator_solve = operator1.solve(operator3)
self.assertTrue(isinstance(
    operator_solve,
    linalg_lib.LinearOperatorDiag))
self.assertAllClose([3 / 2., 1.], self.evaluate(operator_solve.diag))

operator_solve = operator3.solve(operator1)
self.assertTrue(isinstance(
    operator_solve,
    linalg_lib.LinearOperatorDiag))
self.assertAllClose([2 / 3., 1.], self.evaluate(operator_solve.diag))
