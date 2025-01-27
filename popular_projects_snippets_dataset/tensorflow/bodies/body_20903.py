# Extracted from ./data/repos/tensorflow/tensorflow/python/training/momentum_test.py
for dtype in [dtypes.float32, dtypes.float64]:
    # train.MomentumOptimizer is V1 only API.
    with ops.Graph().as_default(), self.cached_session():
        var0_np = np.array([1.0, 2.0], dtype=dtype.as_numpy_dtype)
        var1_np = np.array([3.0, 4.0], dtype=dtype.as_numpy_dtype)
        accum0_np = np.array([0.0, 0.0], dtype=dtype.as_numpy_dtype)
        accum1_np = np.array([0.0, 0.0], dtype=dtype.as_numpy_dtype)
        grads = []
        for t in range(1, 5):
            grads.append(var0_np * 10)
            var0_np, accum0_np = self._update_nesterov_momentum_numpy(
                var0_np, accum0_np, var0_np * 10, 2.0, 0.9)
            var1_np, accum1_np = self._update_nesterov_momentum_numpy(
                var1_np, accum1_np, 3, 2.0, 0.9)
        var0_np = np.array([1.0, 2.0], dtype=dtype.as_numpy_dtype)
        var1_np = np.array([3.0, 4.0], dtype=dtype.as_numpy_dtype)
        accum0_np = np.array([0.0, 0.0], dtype=dtype.as_numpy_dtype)
        accum1_np = np.array([0.0, 0.0], dtype=dtype.as_numpy_dtype)
        var0 = variables.Variable(var0_np)
        var1 = variables.Variable(var1_np)
        mom_op = momentum_lib.MomentumOptimizer(
            learning_rate=2.0, momentum=0.9, use_nesterov=True)
        x_feed = array_ops.placeholder(dtype)
        y_feed = indexed_slices.IndexedSlices(x_feed,
                                              constant_op.constant([0, 1]),
                                              constant_op.constant([2]))
        grads_and_vars = [(y_feed, var0),
                          (constant_op.constant([3.0, 3.0], dtype=dtype), var1)]
        opt_update = mom_op.apply_gradients(grads_and_vars)
        self.evaluate(variables.global_variables_initializer())
        for t in range(1, 5):
            opt_update.run(feed_dict={x_feed: grads[t - 1]})
            var0_np, accum0_np = self._update_nesterov_momentum_numpy(
                var0_np, accum0_np, var0_np * 10, 2.0, 0.9)
            var1_np, accum1_np = self._update_nesterov_momentum_numpy(
                var1_np, accum1_np, 3, 2.0, 0.9)
            self.assertAllClose(var0_np, self.evaluate(var0))
            self.assertAllClose(var1_np, self.evaluate(var1))
