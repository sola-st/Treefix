# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_addition_test.py
op_a = linalg.LinearOperatorDiag(
    [1., 1.], is_positive_definite=True, name="A")
op_b = linalg.LinearOperatorDiag(
    [2., 2.], is_positive_definite=True, name="B")
with self.cached_session():
    op_sum = add_operators([op_a, op_b])
    self.assertEqual(1, len(op_sum))
    op = op_sum[0]
    self.assertIsInstance(op, linalg_lib.LinearOperatorDiag)
    self.assertAllClose([[3., 0.], [0., 3.]], op.to_dense())
    # Adding positive definite operators produces positive def.
    self.assertTrue(op.is_positive_definite)
    # Real diagonal ==> self-adjoint.
    self.assertTrue(op.is_self_adjoint)
    # Positive definite ==> non-singular
    self.assertTrue(op.is_non_singular)
    # Enforce particular name for this simple case
    self.assertEqual("Add/B__A/", op.name)
