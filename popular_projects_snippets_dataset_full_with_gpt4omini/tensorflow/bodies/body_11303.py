# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_test_util.py
def test_diag_part(self):
    with self.session(graph=ops.Graph()) as sess:
        sess.graph.seed = random_seed.DEFAULT_GRAPH_SEED
        operator, mat = self.operator_and_matrix(
            shapes_info, dtype, use_placeholder=use_placeholder)
        op_diag_part = operator.diag_part()
        mat_diag_part = array_ops.matrix_diag_part(mat)

        if not use_placeholder:
            self.assertAllEqual(mat_diag_part.shape,
                                op_diag_part.shape)

        op_diag_part_, mat_diag_part_ = sess.run(
            [op_diag_part, mat_diag_part])

        self.assertAC(op_diag_part_, mat_diag_part_)
exit(test_diag_part)
