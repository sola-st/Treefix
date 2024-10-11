# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/self_adjoint_eig_op_test.py
all_ops = []
with self.session():
    for compute_v_ in True, False:
        matrix1 = random_ops.random_normal([5, 5], seed=42)
        matrix2 = random_ops.random_normal([5, 5], seed=42)
        if compute_v_:
            e1, v1 = linalg_ops.self_adjoint_eig(matrix1)
            e2, v2 = linalg_ops.self_adjoint_eig(matrix2)
            all_ops += [e1, v1, e2, v2]
        else:
            e1 = linalg_ops.self_adjoint_eigvals(matrix1)
            e2 = linalg_ops.self_adjoint_eigvals(matrix2)
            all_ops += [e1, e2]
    val = self.evaluate(all_ops)
    self.assertAllEqual(val[0], val[2])
    # The algorithm is slightly different for compute_v being True and False,
    # so require approximate equality only here.
    self.assertAllClose(val[2], val[4])
    self.assertAllEqual(val[4], val[5])
    self.assertAllEqual(val[1], val[3])
