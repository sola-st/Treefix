# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_test_util.py
def test_adjoint(self):
    with self.test_session(graph=ops.Graph()) as sess:
        sess.graph.seed = random_seed.DEFAULT_GRAPH_SEED
        operator, mat = self.operator_and_matrix(
            shapes_info, dtype, use_placeholder=use_placeholder)
        op_adjoint = operator.adjoint().to_dense()
        op_adjoint_h = operator.H.to_dense()
        mat_adjoint = linalg.adjoint(mat)
        op_adjoint_v, op_adjoint_h_v, mat_adjoint_v = sess.run(
            [op_adjoint, op_adjoint_h, mat_adjoint])
        self.assertAC(mat_adjoint_v, op_adjoint_v)
        self.assertAC(mat_adjoint_v, op_adjoint_h_v)
exit(test_adjoint)
