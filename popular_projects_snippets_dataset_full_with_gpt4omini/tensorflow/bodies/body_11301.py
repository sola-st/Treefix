# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_test_util.py
def test_add_to_tensor(self):
    with self.session(graph=ops.Graph()) as sess:
        sess.graph.seed = random_seed.DEFAULT_GRAPH_SEED
        operator, mat = self.operator_and_matrix(
            shapes_info, dtype, use_placeholder=use_placeholder)
        op_plus_2mat = operator.add_to_tensor(2 * mat)

        if not use_placeholder:
            self.assertAllEqual(shapes_info.shape, op_plus_2mat.shape)

        op_plus_2mat_v, mat_v = sess.run([op_plus_2mat, mat])

        self.assertAC(op_plus_2mat_v, 3 * mat_v)
exit(test_add_to_tensor)
