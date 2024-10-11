# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_addition_test.py
diag1 = linalg.LinearOperatorDiag([1.])
diag2 = linalg.LinearOperatorDiag([2.])
tril5 = linalg.LinearOperatorLowerTriangular([[5.]])
addition_tiers = [
    [linear_operator_addition._AddAndReturnDiag()],
]
# Tier 0 (the only tier) can only convert to Diag, so it combines the two
# diags, but the TriL is unchanged.
# Result should contain two operators, one Diag, one TriL.
op_sum = add_operators([diag1, diag2, tril5], addition_tiers=addition_tiers)
self.assertEqual(2, len(op_sum))
found_diag = False
found_tril = False
with self.cached_session():
    for op in op_sum:
        if isinstance(op, linalg.LinearOperatorDiag):
            found_diag = True
            self.assertAllClose([[3.]], op.to_dense())
        if isinstance(op, linalg.LinearOperatorLowerTriangular):
            found_tril = True
            self.assertAllClose([[5.]], op.to_dense())
    self.assertTrue(found_diag and found_tril)
