# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_test_util.py
with self.session(graph=ops.Graph()) as sess:
    sess.graph.seed = random_seed.DEFAULT_GRAPH_SEED
    operator, mat = self.operator_and_matrix(
        shapes_info, dtype, use_placeholder=use_placeholder)
    op_trace = operator.trace()
    mat_trace = math_ops.trace(mat)
    if not use_placeholder:
        self.assertAllEqual(op_trace.shape, mat_trace.shape)
    op_trace_v, mat_trace_v = sess.run([op_trace, mat_trace])
    self.assertAC(op_trace_v, mat_trace_v)
