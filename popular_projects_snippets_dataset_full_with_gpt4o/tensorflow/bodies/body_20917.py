# Extracted from ./data/repos/tensorflow/tensorflow/python/training/adagrad_da_test.py
for dtype in [dtypes.float32, dtypes.float64]:
    with self.cached_session():
        var0 = resource_variable_ops.ResourceVariable([[1.0, 2.0]], dtype=dtype)
        global_step = resource_variable_ops.ResourceVariable(
            0, dtype=dtypes.int64)
        x = constant_op.constant([[4.0], [5.0]], dtype=dtype)
        pred = math_ops.matmul(embedding_ops.embedding_lookup([var0], [0]), x)
        loss = pred * pred
        sgd_op = adagrad_da.AdagradDAOptimizer(
            1.0, global_step).minimize(loss)
        self.evaluate(variables.global_variables_initializer())
        # Fetch params to validate initial values
        self.assertAllCloseAccordingToType([[1.0, 2.0]], self.evaluate(var0))
        # Run 1 step of sgd
        sgd_op.run()
        # Validate updated params
        self.assertAllCloseAccordingToType([[-1, -1]],
                                           self.evaluate(var0),
                                           rtol=0.01)
