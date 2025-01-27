# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_addition_test.py
diag1 = linalg.LinearOperatorDiag([1., 2.])
diag2 = linalg.LinearOperatorDiag([-1., 3.])
hints = linear_operator_addition._Hints(
    is_positive_definite=False, is_non_singular=False)

self.assertTrue(self._adder.can_add(diag1, diag2))
operator = self._adder.add(diag1, diag2, "my_operator", hints)
self.assertIsInstance(operator, linalg.LinearOperatorFullMatrix)

with self.cached_session():
    self.assertAllClose([[0., 0.], [0., 5.]], operator.to_dense())
self.assertFalse(operator.is_positive_definite)
self.assertFalse(operator.is_non_singular)
self.assertEqual("my_operator", operator.name)
