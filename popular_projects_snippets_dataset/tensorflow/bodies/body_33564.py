# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_addition_test.py
op1 = linalg.LinearOperatorDiag(
    [1., 1.], is_positive_definite=True, name="op1")
op2 = linalg.LinearOperatorDiag(
    [2., 2.], is_positive_definite=True, name="op2")
op3 = linalg.LinearOperatorDiag(
    [3., 3.], is_positive_definite=True, name="op3")
with self.cached_session():
    op_sum = add_operators([op1, op2, op3])
    self.assertEqual(1, len(op_sum))
    op = op_sum[0]
    self.assertTrue(isinstance(op, linalg_lib.LinearOperatorDiag))
    self.assertAllClose([[6., 0.], [0., 6.]], op.to_dense())
    # Adding positive definite operators produces positive def.
    self.assertTrue(op.is_positive_definite)
    # Real diagonal ==> self-adjoint.
    self.assertTrue(op.is_self_adjoint)
    # Positive definite ==> non-singular
    self.assertTrue(op.is_non_singular)
