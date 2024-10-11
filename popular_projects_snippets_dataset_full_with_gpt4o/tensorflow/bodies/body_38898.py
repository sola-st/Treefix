# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
with self.cached_session() as sess:
    q = data_flow_ops.SparseConditionalAccumulator(
        dtypes_lib.float32, name="Q", shape=tensor_shape.TensorShape([3, 3]))
    accum_op = q.apply_grad(
        grad_indices=constant_op.constant(
            [0, 2], dtype=dtypes_lib.int32),
        grad_values=constant_op.constant(
            [[0, 0, 1], [3, 0, 4]], dtype=dtypes_lib.float32),
        grad_shape=constant_op.constant(
            [3, 3], dtype=dtypes_lib.int32))
    accum_op.run()
    accum_op = q.apply_indexed_slices_grad(
        indexed_slices.IndexedSlices(
            indices=constant_op.constant(
                [0, 2], dtype=dtypes_lib.int32),
            values=constant_op.constant(
                [[0, 0, 1], [3, 0, 4]], dtype=dtypes_lib.float32),
            dense_shape=constant_op.constant(
                [3, 3], dtype=dtypes_lib.int32)))
    accum_op.run()
    self.assertEqual(q.num_accumulated().eval(), 2)

    val = self.evaluate(q.take_indexed_slices_grad(1))
    self.assertAllEqual(val.indices, [0, 2])
    self.assertAllEqual(val.values, [[0, 0, 1], [3, 0, 4]])
    self.assertAllEqual(val.dense_shape, [3, 3])
