# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_test_util.py
with self.session(graph=ops.Graph()) as sess:
    sess.graph.seed = random_seed.DEFAULT_GRAPH_SEED
    operator, mat = self.operator_and_matrix(
        shapes_info, dtype, use_placeholder=use_placeholder)
    op_inverse_v, mat_inverse_v = sess.run([
        operator.inverse().to_dense(), linalg.inv(mat)])
    self.assertAC(op_inverse_v, mat_inverse_v, check_dtype=True)
