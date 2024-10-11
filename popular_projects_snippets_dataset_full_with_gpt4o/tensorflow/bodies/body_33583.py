# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_addition_test.py
diag = linalg.LinearOperatorDiag([1., 2.])
tril = linalg.LinearOperatorLowerTriangular([[10., 0.], [30., 0.]])
hints = linear_operator_addition._Hints(
    is_positive_definite=True, is_non_singular=True)

self.assertTrue(self._adder.can_add(diag, diag))
self.assertTrue(self._adder.can_add(diag, tril))
operator = self._adder.add(diag, tril, "my_operator", hints)
self.assertIsInstance(operator, linalg.LinearOperatorLowerTriangular)

with self.cached_session():
    self.assertAllClose([[11., 0.], [30., 2.]], operator.to_dense())
self.assertTrue(operator.is_positive_definite)
self.assertTrue(operator.is_non_singular)
self.assertEqual("my_operator", operator.name)
