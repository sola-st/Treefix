# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_addition_test.py
op0 = linalg.LinearOperatorFullMatrix(
    [[-1., -1.], [-1., -1.]], name="matrix")
op1 = linalg.LinearOperatorDiag([1., 1.], name="diag_a")
op2 = linalg.LinearOperatorLowerTriangular(
    [[2., 0.], [1.5, 2.]], name="tril")
op3 = linalg.LinearOperatorDiag([3., 3.], name="diag_b")
with self.cached_session():
    op_sum = add_operators([op0, op1, op2, op3], operator_name="my_operator")
    self.assertEqual(1, len(op_sum))
    op = op_sum[0]
    self.assertIsInstance(op, linalg_lib.LinearOperatorFullMatrix)
    self.assertAllClose([[5., -1.], [0.5, 5.]], op.to_dense())
    self.assertEqual("my_operator", op.name)
