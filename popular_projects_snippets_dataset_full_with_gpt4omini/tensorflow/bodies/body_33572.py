# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_addition_test.py
diag1 = linalg.LinearOperatorDiag([1.])
diag2 = linalg.LinearOperatorDiag([1.])
tril = linalg.LinearOperatorLowerTriangular([[1.]])
addition_tiers = [
    [linear_operator_addition._AddAndReturnTriL()],
    [linear_operator_addition._AddAndReturnDiag()],
    [_BadAdder()],
]
# Tier 0 could convert to TriL, and this converted everything to TriL,
# including the Diags.
# Tier 1 was never used.
# Tier 2 was never used (therefore, _BadAdder didn't raise).
op_sum = add_operators([diag1, diag2, tril], addition_tiers=addition_tiers)
self.assertEqual(1, len(op_sum))
self.assertIsInstance(op_sum[0], linalg.LinearOperatorLowerTriangular)
