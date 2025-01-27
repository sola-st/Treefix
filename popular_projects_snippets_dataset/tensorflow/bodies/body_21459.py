# Extracted from ./data/repos/tensorflow/tensorflow/python/training/adam_test.py
for dtype in [dtypes.half, dtypes.float32, dtypes.float64]:
    with self.cached_session():
        # Initialize variables for numpy implementation.
        m0, v0, m1, v1 = 0.0, 0.0, 0.0, 0.0
        var0_np = np.array([1.0, 2.0], dtype=dtype.as_numpy_dtype)
        grads0_np = np.array([0.1, 0.1], dtype=dtype.as_numpy_dtype)
        var1_np = np.array([3.0, 4.0], dtype=dtype.as_numpy_dtype)
        grads1_np = np.array([0.01, 0.01], dtype=dtype.as_numpy_dtype)

        if use_resource:
            var0 = resource_variable_ops.ResourceVariable(var0_np)
            var1 = resource_variable_ops.ResourceVariable(var1_np)
        else:
            var0 = variables.RefVariable(var0_np)
            var1 = variables.RefVariable(var1_np)
        grads0_np_indices = np.array([0, 1], dtype=np.int32)
        grads0 = indexed_slices.IndexedSlices(
            constant_op.constant(grads0_np),
            constant_op.constant(grads0_np_indices), constant_op.constant([2]))
        grads1_np_indices = np.array([0, 1], dtype=np.int32)
        grads1 = indexed_slices.IndexedSlices(
            constant_op.constant(grads1_np),
            constant_op.constant(grads1_np_indices), constant_op.constant([2]))
        opt = adam.AdamOptimizer()
        update = opt.apply_gradients(zip([grads0, grads1], [var0, var1]))
        self.evaluate(variables.global_variables_initializer())

        # Fetch params to validate initial values
        self.assertAllClose([1.0, 2.0], self.evaluate(var0))
        self.assertAllClose([3.0, 4.0], self.evaluate(var1))

        beta1_power, beta2_power = opt._get_beta_accumulators()

        # Run 3 steps of Adam
        for t in range(1, 4):
            self.assertAllCloseAccordingToType(0.9**t, self.evaluate(beta1_power))
            self.assertAllCloseAccordingToType(0.999**t,
                                               self.evaluate(beta2_power))
            update.run()

            var0_np, m0, v0 = adam_update_numpy(var0_np, grads0_np, t, m0, v0)
            var1_np, m1, v1 = adam_update_numpy(var1_np, grads1_np, t, m1, v1)

            # Validate updated params
            self.assertAllCloseAccordingToType(var0_np, self.evaluate(var0))
            self.assertAllCloseAccordingToType(var1_np, self.evaluate(var1))
