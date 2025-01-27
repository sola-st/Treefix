# Extracted from ./data/repos/tensorflow/tensorflow/python/training/gradient_descent_test.py
for dtype in [dtypes.half, dtypes.float32, dtypes.float64]:
    # train.GradientDescentOptimizer is V1 only API.
    with ops.Graph().as_default(), self.cached_session():
        var0 = variables.Variable([1.0, 2.0], dtype=dtype)
        var1 = variables.Variable([3.0, 4.0], dtype=dtype)
        grads0 = constant_op.constant([0.1, 0.1], dtype=dtype)
        grads1 = constant_op.constant([0.01, 0.01], dtype=dtype)
        lrate = constant_op.constant(3.0)
        sgd_op = gradient_descent.GradientDescentOptimizer(
            lrate).apply_gradients(zip([grads0, grads1], [var0, var1]))
        self.evaluate(variables.global_variables_initializer())
        # Fetch params to validate initial values
        self.assertAllCloseAccordingToType([1.0, 2.0], self.evaluate(var0))
        self.assertAllCloseAccordingToType([3.0, 4.0], self.evaluate(var1))
        # Run 1 step of sgd
        sgd_op.run()
        # Validate updated params
        self.assertAllCloseAccordingToType([1.0 - 3.0 * 0.1, 2.0 - 3.0 * 0.1],
                                           self.evaluate(var0))
        self.assertAllCloseAccordingToType([3.0 - 3.0 * 0.01, 4.0 - 3.0 * 0.01],
                                           self.evaluate(var1))
