# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
with self.cached_session() as sess:
    q = data_flow_ops.SparseConditionalAccumulator(
        dtypes_lib.float32, name="Q", shape=tensor_shape.TensorShape([3, 3]))

    x_indices = array_ops.placeholder(dtypes_lib.int64)
    x_values = array_ops.placeholder(dtypes_lib.float32)

    accum_op = q.apply_grad(grad_indices=x_indices, grad_values=x_values)

    with self.assertRaisesRegex(
        errors_impl.InvalidArgumentError,
        "Input indices should be vector but received shape:"):
        sess.run(accum_op,
                 feed_dict={
                     x_indices: [[0, 1], [1, 0]],
                     x_values: np.array([1, 2]).astype(np.float32)
                 })
