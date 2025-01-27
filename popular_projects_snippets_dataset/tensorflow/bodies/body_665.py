# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/momentum_test.py
for dtype in self.float_types:
    with self.session(), self.test_scope():
        var0 = resource_variable_ops.ResourceVariable([0.1, 0.2], dtype=dtype)
        var1 = resource_variable_ops.ResourceVariable([0.3, 0.4], dtype=dtype)
        var0_np = np.array([0.1, 0.2], dtype=dtype)
        var1_np = np.array([0.3, 0.4], dtype=dtype)
        accum0_np = np.array([0.0, 0.0], dtype=dtype)
        accum1_np = np.array([0.0, 0.0], dtype=dtype)
        cost = 0.4 * var0 * var0 + 0.9 * var1
        global_step = resource_variable_ops.ResourceVariable(
            array_ops.zeros([], dtypes.int32), name="global_step")
        mom_op = momentum_lib.MomentumOptimizer(
            learning_rate=0.1, momentum=0.9, use_nesterov=True)
        opt_op = mom_op.minimize(cost, global_step, [var0, var1])
        self.evaluate(variables.global_variables_initializer())
        for _ in range(1, 5):
            opt_op.run()
            var0_np, accum0_np = self._update_nesterov_momentum_numpy(
                var0_np, accum0_np, var0_np * 0.8, 0.1, 0.9)
            var1_np, accum1_np = self._update_nesterov_momentum_numpy(
                var1_np, accum1_np, 0.9, 0.1, 0.9)
            self.assertAllCloseAccordingToType(var0_np, self.evaluate(var0))
            self.assertAllCloseAccordingToType(var1_np, self.evaluate(var1))
