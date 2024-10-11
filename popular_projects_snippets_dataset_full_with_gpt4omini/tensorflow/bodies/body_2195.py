# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/ftrl_test.py
for dtype in self.float_types:
    with self.session(), self.test_scope():
        var0 = resource_variable_ops.ResourceVariable([1.0, 2.0], dtype=dtype)
        var1 = resource_variable_ops.ResourceVariable([4.0, 3.0], dtype=dtype)
        grads0 = constant_op.constant([0.1, 0.2], dtype=dtype)
        grads1 = constant_op.constant([0.01, 0.02], dtype=dtype)
        opt = ftrl.FtrlOptimizer(
            3.0,
            initial_accumulator_value=0.1,
            l1_regularization_strength=0.0,
            l2_regularization_strength=0.0)
        ftrl_update = opt.apply_gradients(zip([grads0, grads1], [var0, var1]))
        self.evaluate(variables.global_variables_initializer())
        # Fetch params to validate initial values
        self.assertAllClose([1.0, 2.0], self.evaluate(var0))
        self.assertAllClose([4.0, 3.0], self.evaluate(var1))

        # Run 3 steps FTRL
        for _ in range(3):
            ftrl_update.run()

        # Validate updated params
        self.assertAllCloseAccordingToType(
            np.array([-2.55607247, -3.98729396]),
            self.evaluate(var0),
            1e-5,
            1e-5,
            float_rtol=1e-4)
        self.assertAllCloseAccordingToType(
            np.array([-0.28232238, -0.56096673]), self.evaluate(var1), 1e-5,
            1e-5)
