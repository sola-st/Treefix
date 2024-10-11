# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
with self.cached_session():
    q = data_flow_ops.SparseConditionalAccumulator(
        dtypes_lib.float32, name="Q", shape=tensor_shape.TensorShape([3, 3]))
    accum_op = q.apply_indexed_slices_grad(
        indexed_slices.IndexedSlices(
            indices=[0, 2],
            values=np.array([[0, 0, 1], [3, 0, 4]]).astype(np.float32)))
    accum_op.run()
    self.assertEqual(q.num_accumulated().eval(), 1)
