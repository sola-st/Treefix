# Extracted from ./data/repos/tensorflow/tensorflow/python/training/ftrl_test.py
"""Verifies that l2 shrinkage in FTRL does not change lr schedule."""
# The v1 optimizers do not support eager execution
with ops.Graph().as_default():
    for dtype in [dtypes.half, dtypes.float32]:
        with self.cached_session():
            var0 = variables.Variable([1.0, 2.0], dtype=dtype)
            var1 = variables.Variable([1.0, 2.0], dtype=dtype)
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

            v0_val, v1_val = self.evaluate([var0, var1])
            self.assertAllCloseAccordingToType([1.0, 2.0], v0_val)
            self.assertAllCloseAccordingToType([1.0, 2.0], v1_val)

            # Run 10 steps FTRL
            for _ in range(10):
                update0.run()
                update1.run()

            v0_val, v1_val = self.evaluate([var0, var1])
            # var0 is experiencing L2 shrinkage so it should be smaller than var1
            # in magnitude.
            self.assertTrue((v0_val**2 < v1_val**2).all())
            accum0 = list(self.evaluate(opt0._slots)["accum"].values())[0]
            accum1 = list(self.evaluate(opt1._slots)["accum"].values())[0]
            # L2 shrinkage should not change how we update grad accumulator.
            self.assertAllCloseAccordingToType(accum0, accum1)
