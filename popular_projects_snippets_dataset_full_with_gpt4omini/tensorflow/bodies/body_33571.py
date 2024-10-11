# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_addition_test.py
diag1 = linalg.LinearOperatorDiag([1.])
diag2 = linalg.LinearOperatorDiag([1.])
tril = linalg.LinearOperatorLowerTriangular([[1.]])
addition_tiers = [
    [linear_operator_addition._AddAndReturnDiag()],
    [linear_operator_addition._AddAndReturnTriL()],
    [_BadAdder()],
]
# Should not raise since all were added by tier 1, and the
# _BadAdder) was never reached.
op_sum = add_operators([diag1, diag2, tril], addition_tiers=addition_tiers)
self.assertEqual(1, len(op_sum))
self.assertIsInstance(op_sum[0], linalg.LinearOperatorLowerTriangular)
