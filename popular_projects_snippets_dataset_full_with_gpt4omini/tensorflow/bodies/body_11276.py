# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_test_util.py
with self.session(graph=ops.Graph()) as sess:
    sess.graph.seed = random_seed.DEFAULT_GRAPH_SEED
    operator_a, mat_a = self.operator_and_matrix(
        shapes_info, dtype, use_placeholder=use_placeholder)
    operator_b, mat_b = self.operator_and_matrix(
        shapes_info, dtype, use_placeholder=use_placeholder)

    mat_solve = linear_operator_util.matrix_solve_with_broadcast(mat_a, mat_b)
    op_solve = operator_a.solve(operator_b)
    mat_solve_v, op_solve_v = sess.run([mat_solve, op_solve.to_dense()])

    self.assertIsInstance(op_solve, operator_a.__class__)
    self.assertAC(mat_solve_v, op_solve_v)
