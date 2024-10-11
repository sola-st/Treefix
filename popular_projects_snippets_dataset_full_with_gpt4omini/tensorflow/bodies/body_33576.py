# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_addition_test.py
id1 = linalg.LinearOperatorIdentity(num_rows=2)
id2 = linalg.LinearOperatorIdentity(num_rows=2, batch_shape=[3])
hints = linear_operator_addition._Hints(
    is_positive_definite=True, is_non_singular=True)

self.assertTrue(self._adder.can_add(id1, id2))
operator = self._adder.add(id1, id2, "my_operator", hints)
self.assertIsInstance(operator, linalg.LinearOperatorScaledIdentity)

with self.cached_session():
    self.assertAllClose(2 * linalg_ops.eye(num_rows=2, batch_shape=[3]),
                        operator.to_dense())
self.assertTrue(operator.is_positive_definite)
self.assertTrue(operator.is_non_singular)
self.assertEqual("my_operator", operator.name)
