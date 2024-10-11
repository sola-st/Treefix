# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_test_util.py
with self.session(graph=ops.Graph()) as sess:
    sess.graph.seed = random_seed.DEFAULT_GRAPH_SEED
    operator, mat = self.operator_and_matrix(
        shapes_info, dtype, use_placeholder=use_placeholder)
    op_det = operator.determinant()
    if not use_placeholder:
        self.assertAllEqual(shapes_info.shape[:-2], op_det.shape)
    op_det_v, mat_det_v = sess.run(
        [op_det, linalg_ops.matrix_determinant(mat)])
    self.assertAC(op_det_v, mat_det_v)
