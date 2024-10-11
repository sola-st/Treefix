# Extracted from ./data/repos/tensorflow/tensorflow/python/training/adagrad_test.py
with ops.Graph().as_default():
    for dtype in [dtypes.half, dtypes.float32, dtypes.float64]:
        with self.cached_session():
            var_repeated = resource_variable_ops.ResourceVariable(
                [1.0, 2.0], dtype=dtype)
            loss_repeated = math_ops.reduce_sum(
                embedding_ops.embedding_lookup(var_repeated, [0, 0]))
            var_aggregated = resource_variable_ops.ResourceVariable(
                [1.0, 2.0], dtype=dtype)
            loss_aggregated = 2 * math_ops.reduce_sum(
                embedding_ops.embedding_lookup(var_aggregated, [0]))
            update_op_repeated = adagrad.AdagradOptimizer(
                2.0).minimize(loss_repeated)
            update_op_aggregated = adagrad.AdagradOptimizer(
                2.0).minimize(loss_aggregated)
            self.evaluate(variables.global_variables_initializer())
            self.assertAllCloseAccordingToType(
                self.evaluate(var_repeated), self.evaluate(var_aggregated))
            for _ in range(3):
                update_op_repeated.run()
                update_op_aggregated.run()
                self.assertAllCloseAccordingToType(
                    self.evaluate(var_repeated), self.evaluate(var_aggregated))
