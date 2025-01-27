# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_test_util.py
def test_log_abs_det(self):
    with self.session(graph=ops.Graph()) as sess:
        sess.graph.seed = random_seed.DEFAULT_GRAPH_SEED
        operator, mat = self.operator_and_matrix(
            shapes_info, dtype, use_placeholder=use_placeholder)
        op_log_abs_det = operator.log_abs_determinant()
        _, mat_log_abs_det = linalg.slogdet(mat)
        if not use_placeholder:
            self.assertAllEqual(
                shapes_info.shape[:-2], op_log_abs_det.shape)
        op_log_abs_det_v, mat_log_abs_det_v = sess.run(
            [op_log_abs_det, mat_log_abs_det])
        self.assertAC(op_log_abs_det_v, mat_log_abs_det_v)
exit(test_log_abs_det)
