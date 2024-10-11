# Extracted from ./data/repos/tensorflow/tensorflow/python/training/momentum_test.py
for dtype in [dtypes.float32, dtypes.float64]:
    # train.MomentumOptimizer is V1 only API.
    with ops.Graph().as_default(), self.cached_session():
        var0 = variables.Variable([1.0, 2.0], dtype=dtype)
        var1 = variables.Variable([3.0, 4.0], dtype=dtype)
        var0_np = np.array([1.0, 2.0], dtype=dtype.as_numpy_dtype)
        var1_np = np.array([3.0, 4.0], dtype=dtype.as_numpy_dtype)
        accum0_np = np.array([0.0, 0.0], dtype=dtype.as_numpy_dtype)
        accum1_np = np.array([0.0, 0.0], dtype=dtype.as_numpy_dtype)
        cost = 5 * var0 * var0 + 3 * var1
        global_step = variables.Variable(
            array_ops.zeros([], dtypes.int64), name="global_step")
        mom_op = momentum_lib.MomentumOptimizer(
            learning_rate=2.0, momentum=0.9, use_nesterov=True)
        opt_op = mom_op.minimize(cost, global_step, [var0, var1])
        self.evaluate(variables.global_variables_initializer())
        for t in range(1, 5):
            opt_op.run()
            var0_np, accum0_np = self._update_nesterov_momentum_numpy(
                var0_np, accum0_np, var0_np * 10, 2.0, 0.9)
            var1_np, accum1_np = self._update_nesterov_momentum_numpy(
                var1_np, accum1_np, 3, 2.0, 0.9)
            self.assertAllClose(var0_np, self.evaluate(var0))
            self.assertAllClose(var1_np, self.evaluate(var1))
