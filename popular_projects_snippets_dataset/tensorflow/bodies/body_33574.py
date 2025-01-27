# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_addition_test.py
diag1 = linalg.LinearOperatorDiag([1.])
diag2 = linalg.LinearOperatorDiag([1.])
tril = linalg.LinearOperatorLowerTriangular([[1.]])
addition_tiers = [
    [linear_operator_addition._AddAndReturnDiag()],
    [_BadAdder()],
    [linear_operator_addition._AddAndReturnTriL()],
]
# tril cannot be added in tier 0, and the intermediate tier 1 with the
# BadAdder will catch it and raise.
with self.assertRaisesRegex(AssertionError, "BadAdder.can_add called"):
    add_operators([diag1, diag2, tril], addition_tiers=addition_tiers)
