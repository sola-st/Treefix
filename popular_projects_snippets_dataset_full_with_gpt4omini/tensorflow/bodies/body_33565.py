# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_addition_test.py
op1 = linalg.LinearOperatorDiag(
    [1., 1.], is_non_singular=True, name="diag_a")
op2 = linalg.LinearOperatorLowerTriangular(
    [[2., 0.], [0., 2.]],
    is_self_adjoint=True,
    is_non_singular=True,
    name="tril")
op3 = linalg.LinearOperatorDiag(
    [3., 3.], is_non_singular=True, name="diag_b")
with self.cached_session():
    op_sum = add_operators([op1, op2, op3])
    self.assertEqual(1, len(op_sum))
    op = op_sum[0]
    self.assertIsInstance(op, linalg_lib.LinearOperatorLowerTriangular)
    self.assertAllClose([[6., 0.], [0., 6.]], op.to_dense())

    # The diag operators will be self-adjoint (because real and diagonal).
    # The TriL operator has the self-adjoint hint set.
    self.assertTrue(op.is_self_adjoint)

    # Even though op1/2/3 are non-singular, this does not imply op is.
    # Since no custom hint was provided, we default to None (unknown).
    self.assertEqual(None, op.is_non_singular)
