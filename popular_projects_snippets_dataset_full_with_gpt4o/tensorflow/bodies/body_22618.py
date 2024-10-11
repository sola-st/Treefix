# Extracted from ./data/repos/tensorflow/tensorflow/python/training/ftrl_test.py
# The v1 optimizers do not support eager execution
with ops.Graph().as_default():
    for dtype in [dtypes.half, dtypes.float32]:
        with self.cached_session():
            var0 = variables.Variable([1.0, 2.0], dtype=dtype)
            var1 = variables.Variable([4.0, 3.0], dtype=dtype)
            grads0 = constant_op.constant([0.1, 0.2], dtype=dtype)
            grads1 = constant_op.constant([0.01, 0.02], dtype=dtype)

            opt = ftrl.FtrlOptimizer(
                3.0,
                initial_accumulator_value=0.1,
                l1_regularization_strength=0.001,
                l2_regularization_strength=2.0)
            update = opt.apply_gradients(zip([grads0, grads1], [var0, var1]))
            self.evaluate(variables.global_variables_initializer())

            v0_val, v1_val = self.evaluate([var0, var1])
            self.assertAllCloseAccordingToType([1.0, 2.0], v0_val)
            self.assertAllCloseAccordingToType([4.0, 3.0], v1_val)

            # Run 10 steps FTRL
            for _ in range(10):
                update.run()

            v0_val, v1_val = self.evaluate([var0, var1])
            self.assertAllCloseAccordingToType(
                np.array([-0.24059935, -0.46829352]), v0_val)
            self.assertAllCloseAccordingToType(
                np.array([-0.02406147, -0.04830509]), v1_val)
