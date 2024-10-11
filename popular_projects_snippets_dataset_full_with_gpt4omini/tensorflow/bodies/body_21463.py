# Extracted from ./data/repos/tensorflow/tensorflow/python/training/adam_test.py
with ops.Graph().as_default():
    for dtype in [dtypes.half, dtypes.float32, dtypes.float64]:
        with self.cached_session():
            repeated_index_update_var = variables.Variable(
                [[1.0], [2.0]], dtype=dtype)
            aggregated_update_var = variables.Variable(
                [[1.0], [2.0]], dtype=dtype)
            grad_repeated_index = indexed_slices.IndexedSlices(
                constant_op.constant(
                    [0.1, 0.1], shape=[2, 1], dtype=dtype),
                constant_op.constant([1, 1]),
                constant_op.constant([2, 1]))
            grad_aggregated = indexed_slices.IndexedSlices(
                constant_op.constant(
                    [0.2], shape=[1, 1], dtype=dtype),
                constant_op.constant([1]),
                constant_op.constant([2, 1]))
            repeated_update = adam.AdamOptimizer().apply_gradients(
                [(grad_repeated_index, repeated_index_update_var)])
            aggregated_update = adam.AdamOptimizer().apply_gradients(
                [(grad_aggregated, aggregated_update_var)])
            self.evaluate(variables.global_variables_initializer())
            self.assertAllClose(aggregated_update_var,
                                self.evaluate(repeated_index_update_var))
            for _ in range(3):
                repeated_update.run()
                aggregated_update.run()
                self.assertAllClose(aggregated_update_var,
                                    self.evaluate(repeated_index_update_var))
