# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_diag_test.py
operator1 = linalg_lib.LinearOperatorDiag([2., 3.])
operator2 = linalg_lib.LinearOperatorDiag([1., 2.])
operator3 = linalg_lib.LinearOperatorScaledIdentity(
    num_rows=2, multiplier=3.)
operator_matmul = operator1.matmul(operator2)
self.assertTrue(isinstance(
    operator_matmul,
    linalg_lib.LinearOperatorDiag))
self.assertAllClose([2., 6.], self.evaluate(operator_matmul.diag))

operator_matmul = operator2.matmul(operator1)
self.assertTrue(isinstance(
    operator_matmul,
    linalg_lib.LinearOperatorDiag))
self.assertAllClose([2., 6.], self.evaluate(operator_matmul.diag))

operator_matmul = operator1.matmul(operator3)
self.assertTrue(isinstance(
    operator_matmul,
    linalg_lib.LinearOperatorDiag))
self.assertAllClose([6., 9.], self.evaluate(operator_matmul.diag))

operator_matmul = operator3.matmul(operator1)
self.assertTrue(isinstance(
    operator_matmul,
    linalg_lib.LinearOperatorDiag))
self.assertAllClose([6., 9.], self.evaluate(operator_matmul.diag))
