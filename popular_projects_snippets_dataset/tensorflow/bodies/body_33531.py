# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_identity_test.py
operator1 = linalg_lib.LinearOperatorIdentity(num_rows=2)
operator2 = linalg_lib.LinearOperatorScaledIdentity(
    num_rows=2, multiplier=3.)
self.assertIsInstance(
    operator1.solve(operator1),
    linalg_lib.LinearOperatorIdentity)

self.assertIsInstance(
    operator2.solve(operator2),
    linalg_lib.LinearOperatorScaledIdentity)

operator_solve = operator1.solve(operator2)
self.assertIsInstance(
    operator_solve,
    linalg_lib.LinearOperatorScaledIdentity)
self.assertAllClose(3., self.evaluate(operator_solve.multiplier))

operator_solve = operator2.solve(operator1)
self.assertIsInstance(
    operator_solve,
    linalg_lib.LinearOperatorScaledIdentity)
self.assertAllClose(1. / 3., self.evaluate(operator_solve.multiplier))
