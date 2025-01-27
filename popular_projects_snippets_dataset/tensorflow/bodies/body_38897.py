# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
with self.cached_session() as sess:
    q = data_flow_ops.SparseConditionalAccumulator(
        dtypes_lib.float32, name="Q", shape=[2, None])

    q.apply_grad(
        grad_indices=[0],
        grad_values=np.array(
            [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]]]).astype(np.float32)).run()

    val = self.evaluate(q.take_indexed_slices_grad(1))
    self.assertAllEqual(val.dense_shape, [2, 2, 2, 2])

    q = data_flow_ops.SparseConditionalAccumulator(
        dtypes_lib.float32, name="Q", shape=[None, 2])

    q.apply_grad(
        grad_indices=[0],
        grad_values=np.array(
            [[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]]).astype(
                np.float32)).run()

    val = self.evaluate(q.take_indexed_slices_grad(1))
    self.assertAllEqual(val.dense_shape, [-1, 2, 2, 3])
