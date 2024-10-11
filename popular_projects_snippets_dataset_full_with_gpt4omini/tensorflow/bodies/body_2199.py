# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/ftrl_test.py
"""Verifies that l2 shrinkage in FTRL does not change lr schedule."""
for dtype in self.float_types:
    with self.session(), self.test_scope():
        var0 = resource_variable_ops.ResourceVariable([1.0, 2.0], dtype=dtype)
        var1 = resource_variable_ops.ResourceVariable([1.0, 2.0], dtype=dtype)
        grads0 = constant_op.constant([0.1, 0.2], dtype=dtype)
        grads1 = constant_op.constant([0.1, 0.2], dtype=dtype)

        opt0 = ftrl.FtrlOptimizer(
            3.0,
            initial_accumulator_value=0.1,
            l1_regularization_strength=0.001,
            l2_regularization_strength=2.0,
            l2_shrinkage_regularization_strength=0.1)
        opt1 = ftrl.FtrlOptimizer(
            3.0,
            initial_accumulator_value=0.1,
            l1_regularization_strength=0.001,
            l2_regularization_strength=2.0)
        update0 = opt0.apply_gradients([(grads0, var0)])
        update1 = opt1.apply_gradients([(grads1, var1)])
        self.evaluate(variables.global_variables_initializer())

        self.assertAllCloseAccordingToType([1.0, 2.0], self.evaluate(var0))
        self.assertAllCloseAccordingToType([1.0, 2.0], self.evaluate(var1))

        # Run 10 steps FTRL
        for _ in range(10):
            update0.run()
            update1.run()

        # var0 is experiencing L2 shrinkage so it should be smaller than var1
        # in magnitude.
        self.assertTrue((var0.eval()**2 < self.evaluate(var1)**2).all())
        accum0 = list(opt0._slots["accum"].values())[0].eval()
        accum1 = list(opt1._slots["accum"].values())[0].eval()
        # L2 shrinkage should not change how we update grad accumulator.
        self.assertAllCloseAccordingToType(accum0, accum1)
