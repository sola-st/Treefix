# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
with self.cached_session() as sess:
    q = data_flow_ops.SparseConditionalAccumulator(
        dtypes_lib.float32, name="Q", shape=())

    grad_indexed_slices = indexed_slices.IndexedSlices(
        indices=[0, 1], values=np.array([[1, 0], [0, 2]]).astype(np.float32))
    accum_op = q.apply_indexed_slices_grad(grad_indexed_slices, local_step=0)
    accum_op.run()
    accum_op = q.apply_grad(
        [0, 2],
        np.array([[0, 1], [3, 0]]).astype(np.float32), [3, 2],
        local_step=0)
    accum_op.run()

    takeg_t = q.take_indexed_slices_grad(1)
    val = self.evaluate(takeg_t)
    self.assertAllEqual(val.indices, [0, 1, 2])
    self.assertAllEqual(val.values, [[0.5, 0.5], [0, 2], [3, 0]])
    self.assertAllEqual(val.dense_shape, [-1, 2])

    grad_indexed_slices = indexed_slices.IndexedSlices(
        indices=[0, 1],
        values=np.array([[10, 0], [0, 20]]).astype(np.float32))
    accum_op = q.apply_indexed_slices_grad(grad_indexed_slices, local_step=1)
    accum_op.run()
    accum_op = q.apply_grad(
        [0, 2],
        np.array([[0, 10], [30, 0]]).astype(np.float32), [3, 2],
        local_step=1)
    accum_op.run()

    takeg_t = q.take_indexed_slices_grad(1)
    val = self.evaluate(takeg_t)
    self.assertAllEqual(val.indices, [0, 1, 2])
    self.assertAllEqual(val.values, [[5, 5], [0, 20], [30, 0]])
    self.assertAllEqual(val.dense_shape, [-1, 2])
