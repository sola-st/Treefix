# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/ftrl_test.py
for dtype in self.float_types:
    with self.session(), self.test_scope():
        var0 = resource_variable_ops.ResourceVariable([0.0, 0.0], dtype=dtype)
        var1 = resource_variable_ops.ResourceVariable([0.0, 0.0], dtype=dtype)
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
        self.assertAllClose([0.0, 0.0], self.evaluate(var0))
        self.assertAllClose([0.0, 0.0], self.evaluate(var1))

        # Run 3 steps FTRL
        for _ in range(3):
            ftrl_update.run()

        # Validate updated params
        self.assertAllCloseAccordingToType(
            np.array([-2.60260963, -4.29698515]),
            self.evaluate(var0),
            float_rtol=1e-4,
            half_rtol=1e-2)
        self.assertAllCloseAccordingToType(
            np.array([-0.28432083, -0.56694895]),
            self.evaluate(var1),
            float_rtol=1e-5,
            half_rtol=1e-2)
