# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_identity_test.py
operator1 = linalg_lib.LinearOperatorIdentity(num_rows=2)
operator2 = linalg_lib.LinearOperatorScaledIdentity(
    num_rows=2, multiplier=3.)
self.assertIsInstance(
    operator1.matmul(operator1),
    linalg_lib.LinearOperatorIdentity)

self.assertIsInstance(
    operator1.matmul(operator1),
    linalg_lib.LinearOperatorIdentity)

self.assertIsInstance(
    operator2.matmul(operator2),
    linalg_lib.LinearOperatorScaledIdentity)

operator_matmul = operator1.matmul(operator2)
self.assertIsInstance(
    operator_matmul,
    linalg_lib.LinearOperatorScaledIdentity)
self.assertAllClose(3., self.evaluate(operator_matmul.multiplier))

operator_matmul = operator2.matmul(operator1)
self.assertIsInstance(
    operator_matmul,
    linalg_lib.LinearOperatorScaledIdentity)
self.assertAllClose(3., self.evaluate(operator_matmul.multiplier))
