# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_test_util.py
with self.session(graph=ops.Graph()) as sess:
    sess.graph.seed = random_seed.DEFAULT_GRAPH_SEED
    operator, mat = self.operator_and_matrix(
        shapes_info, dtype, use_placeholder=use_placeholder)
    op_dense = operator.to_dense()
    if not use_placeholder:
        self.assertAllEqual(shapes_info.shape, op_dense.shape)
    op_dense_v, mat_v = sess.run([op_dense, mat])
    self.assertAC(op_dense_v, mat_v)
