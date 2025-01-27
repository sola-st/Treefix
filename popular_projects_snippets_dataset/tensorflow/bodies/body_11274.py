# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_test_util.py
with self.session(graph=ops.Graph()) as sess:
    sess.graph.seed = random_seed.DEFAULT_GRAPH_SEED
    operator_a, mat_a = self.operator_and_matrix(
        shapes_info, dtype, use_placeholder=use_placeholder)
    operator_b, mat_b = self.operator_and_matrix(
        shapes_info, dtype, use_placeholder=use_placeholder)

    mat_matmul = math_ops.matmul(mat_a, mat_b)
    op_matmul = operator_a.matmul(operator_b)
    mat_matmul_v, op_matmul_v = sess.run([mat_matmul, op_matmul.to_dense()])

    self.assertIsInstance(op_matmul, operator_a.__class__)
    self.assertAC(mat_matmul_v, op_matmul_v)
