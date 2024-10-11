# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_addition_test.py
diag1 = rng.rand(2, 3, 4)
diag2 = rng.rand(4)
op1 = linalg.LinearOperatorDiag(diag1)
op2 = linalg.LinearOperatorDiag(diag2)
hints = linear_operator_addition._Hints(
    is_positive_definite=True, is_non_singular=True)

self.assertTrue(self._adder.can_add(op1, op2))
operator = self._adder.add(op1, op2, "my_operator", hints)
self.assertIsInstance(operator, linalg.LinearOperatorDiag)

with self.cached_session():
    self.assertAllClose(
        linalg.LinearOperatorDiag(diag1 + diag2).to_dense(),
        operator.to_dense())
self.assertTrue(operator.is_positive_definite)
self.assertTrue(operator.is_non_singular)
self.assertEqual("my_operator", operator.name)
