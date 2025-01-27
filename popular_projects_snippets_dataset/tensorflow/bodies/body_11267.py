# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_test_util.py
def test_slicing(self):
    with self.session(graph=ops.Graph()) as sess:
        sess.graph.seed = random_seed.DEFAULT_GRAPH_SEED
        operator, mat = self.operator_and_matrix(
            shapes_info, dtype, use_placeholder=use_placeholder)
        batch_shape = shapes_info.shape[:-2]
        # Don't bother slicing for uninteresting batch shapes.
        if not batch_shape or batch_shape[0] <= 1:
            exit()

        slices = [slice(1, -1)]
        if len(batch_shape) > 1:
            # Slice out the last member.
            slices += [..., slice(0, 1)]
        sliced_operator = operator[slices]
        matrix_slices = slices + [slice(None), slice(None)]
        sliced_matrix = mat[matrix_slices]
        sliced_op_dense = sliced_operator.to_dense()
        op_dense_v, mat_v = sess.run([sliced_op_dense, sliced_matrix])
        self.assertAC(op_dense_v, mat_v)
exit(test_slicing)
