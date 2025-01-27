# Extracted from ./data/repos/tensorflow/tensorflow/python/training/rmsprop_test.py
# TODO(yori): Use ParameterizedTest when available
for (dtype, learning_rate, decay,
     momentum, epsilon, centered, _) in _TESTPARAMS:
    with test_util.use_gpu():
        # Initialize variables for numpy implementation.
        var0_np = np.array([1.0, 2.0], dtype=dtype.as_numpy_dtype)
        grads0_np = np.array([0.1], dtype=dtype.as_numpy_dtype)
        var1_np = np.array([3.0, 4.0], dtype=dtype.as_numpy_dtype)
        grads1_np = np.array([0.01], dtype=dtype.as_numpy_dtype)

        var0 = variables.Variable(var0_np)
        var1 = variables.Variable(var1_np)
        grads0_np_indices = np.array([0], dtype=np.int32)
        grads0 = indexed_slices.IndexedSlices(
            constant_op.constant(grads0_np),
            constant_op.constant(grads0_np_indices), constant_op.constant([1]))
        grads1_np_indices = np.array([1], dtype=np.int32)
        grads1 = indexed_slices.IndexedSlices(
            constant_op.constant(grads1_np),
            constant_op.constant(grads1_np_indices), constant_op.constant([1]))
        opt = rmsprop.RMSPropOptimizer(
            learning_rate=learning_rate,
            decay=decay,
            momentum=momentum,
            epsilon=epsilon,
            centered=centered)
        update = opt.apply_gradients(zip([grads0, grads1], [var0, var1]))
        self.evaluate(variables.global_variables_initializer())

        mg0 = opt.get_slot(var0, "mg")
        self.assertEqual(mg0 is not None, centered)
        mg1 = opt.get_slot(var1, "mg")
        self.assertEqual(mg1 is not None, centered)
        rms0 = opt.get_slot(var0, "rms")
        self.assertTrue(rms0 is not None)
        rms1 = opt.get_slot(var1, "rms")
        self.assertTrue(rms1 is not None)
        mom0 = opt.get_slot(var0, "momentum")
        self.assertTrue(mom0 is not None)
        mom1 = opt.get_slot(var1, "momentum")
        self.assertTrue(mom1 is not None)

        mg0_np = np.array([0.0, 0.0], dtype=dtype.as_numpy_dtype)
        mg1_np = np.array([0.0, 0.0], dtype=dtype.as_numpy_dtype)
        rms0_np = np.array([1.0, 1.0], dtype=dtype.as_numpy_dtype)
        rms1_np = np.array([1.0, 1.0], dtype=dtype.as_numpy_dtype)
        mom0_np = np.array([0.0, 0.0], dtype=dtype.as_numpy_dtype)
        mom1_np = np.array([0.0, 0.0], dtype=dtype.as_numpy_dtype)

        # Fetch params to validate initial values
        self.assertAllClose([1.0, 2.0], self.evaluate(var0))
        self.assertAllClose([3.0, 4.0], self.evaluate(var1))

        # Run 4 steps of RMSProp
        for _ in range(1, 5):
            self.evaluate(update)

            var0_np, mg0_np, rms0_np, mom0_np = self._sparse_rmsprop_update_numpy(
                var0_np, grads0_np_indices, grads0_np, mg0_np, rms0_np, mom0_np,
                learning_rate, decay, momentum, epsilon, centered)
            var1_np, mg1_np, rms1_np, mom1_np = self._sparse_rmsprop_update_numpy(
                var1_np, grads1_np_indices, grads1_np, mg1_np, rms1_np, mom1_np,
                learning_rate, decay, momentum, epsilon, centered)

            # Validate updated params
            if centered:
                self.assertAllCloseAccordingToType(mg0_np, self.evaluate(mg0))
                self.assertAllCloseAccordingToType(mg1_np, self.evaluate(mg1))
            self.assertAllCloseAccordingToType(rms0_np, self.evaluate(rms0))
            self.assertAllCloseAccordingToType(rms1_np, self.evaluate(rms1))
            self.assertAllCloseAccordingToType(mom0_np, self.evaluate(mom0))
            self.assertAllCloseAccordingToType(mom1_np, self.evaluate(mom1))
            self.assertAllCloseAccordingToType(var0_np, self.evaluate(var0))
            self.assertAllCloseAccordingToType(var1_np, self.evaluate(var1))
