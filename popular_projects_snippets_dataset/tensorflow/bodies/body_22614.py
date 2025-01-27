# Extracted from ./data/repos/tensorflow/tensorflow/python/training/ftrl_test.py
# The v1 optimizers do not support eager execution
with ops.Graph().as_default():
    for dtype in [dtypes.half, dtypes.float32, dtypes.float64]:
        with self.cached_session():
            var0 = resource_variable_ops.ResourceVariable([[1.0, 2.0]],
                                                          dtype=dtype)
            x = constant_op.constant([[4.0], [5.0]], dtype=dtype)
            pred = math_ops.matmul(embedding_ops.embedding_lookup([var0], [0]), x)
            loss = pred * pred
            sgd_op = ftrl.FtrlOptimizer(1.0).minimize(loss)
            self.evaluate(variables.global_variables_initializer())
            # Fetch params to validate initial values
            self.assertAllCloseAccordingToType([[1.0, 2.0]], self.evaluate(var0))
            # Run 1 step of sgd
            sgd_op.run()
            # Validate updated params
            self.assertAllCloseAccordingToType([[0, 1]],
                                               self.evaluate(var0),
                                               atol=0.01)
