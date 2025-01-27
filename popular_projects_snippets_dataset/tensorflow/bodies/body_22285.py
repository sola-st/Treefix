# Extracted from ./data/repos/tensorflow/tensorflow/python/training/optimizer_test.py
for dtype in [dtypes.half, dtypes.float32, dtypes.float64]:
    with self.cached_session():
        var0 = variables.Variable([1.0, 2.0], dtype=dtype)
        var1 = variables.Variable([3.0, 4.0], dtype=dtype)
        cost = 5 * var0 + 3 * var1
        global_step = variables.Variable(
            array_ops.zeros([], dtypes.int64), name='global_step')
        sgd_op = gradient_descent.GradientDescentOptimizer(3.0)
        opt_op = sgd_op.minimize(
            cost,
            global_step, [var0, var1],
            aggregation_method=gradients_util.AggregationMethod.
            EXPERIMENTAL_ACCUMULATE_N)

        self.evaluate(variables.global_variables_initializer())
        # Fetch params to validate initial values
        self.assertAllClose([1.0, 2.0], self.evaluate(var0))
        self.assertAllClose([3.0, 4.0], self.evaluate(var1))
        # Run 1 step of sgd through optimizer
        opt_op.run()
        # Validate updated params
        self.assertAllClose([-14., -13.], self.evaluate(var0))
        self.assertAllClose([-6., -5.], self.evaluate(var1))
