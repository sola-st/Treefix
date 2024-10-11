# Extracted from ./data/repos/tensorflow/tensorflow/python/training/ftrl_test.py
# The v1 optimizers do not support eager execution
with ops.Graph().as_default():
    for dtype in [dtypes.half, dtypes.float32]:
        with self.cached_session():
            if use_resource:
                var0 = resource_variable_ops.ResourceVariable([0.0, 0.0],
                                                              dtype=dtype)
                var1 = resource_variable_ops.ResourceVariable([0.0, 0.0],
                                                              dtype=dtype)
            else:
                var0 = variables.Variable([0.0, 0.0], dtype=dtype)
                var1 = variables.Variable([0.0, 0.0], dtype=dtype)
            grads0 = constant_op.constant([0.1, 0.2], dtype=dtype)
            grads1 = constant_op.constant([0.01, 0.02], dtype=dtype)
            opt = ftrl.FtrlOptimizer(
                3.0,
                initial_accumulator_value=0.1,
                l1_regularization_strength=0.0,
                l2_regularization_strength=0.0)
            update = opt.apply_gradients(zip([grads0, grads1], [var0, var1]))
            self.evaluate(variables.global_variables_initializer())

            v0_val, v1_val = self.evaluate([var0, var1])
            self.assertAllClose([0.0, 0.0], v0_val)
            self.assertAllClose([0.0, 0.0], v1_val)

            # Run 3 steps FTRL
            for _ in range(3):
                update.run()

            v0_val, v1_val = self.evaluate([var0, var1])
            self.assertAllCloseAccordingToType(
                np.array([-2.60260963, -4.29698515]), v0_val, half_rtol=1e-2)
            self.assertAllCloseAccordingToType(
                np.array([-0.28432083, -0.56694895]), v1_val)
