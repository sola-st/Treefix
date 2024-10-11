# Extracted from ./data/repos/tensorflow/tensorflow/python/training/rmsprop_test.py
for dtype in [dtypes.half, dtypes.float32]:
    with test_util.use_gpu():
        var0 = variables.Variable([1.0, 2.0], dtype=dtype)
        var1 = variables.Variable([3.0, 4.0], dtype=dtype)
        grads0 = constant_op.constant([0.1, 0.1], dtype=dtype)
        grads1 = constant_op.constant([0.01, 0.01], dtype=dtype)

        opt = rmsprop.RMSPropOptimizer(
            learning_rate=2.0, decay=0.9, momentum=0.5, epsilon=1e-5)
        update = opt.apply_gradients(zip([grads0, grads1], [var0, var1]))
        self.evaluate(variables.global_variables_initializer())

        rms0 = opt.get_slot(var0, "rms")
        self.assertTrue(rms0 is not None)
        rms1 = opt.get_slot(var1, "rms")
        self.assertTrue(rms1 is not None)
        mom0 = opt.get_slot(var0, "momentum")
        self.assertTrue(mom0 is not None)
        mom1 = opt.get_slot(var1, "momentum")
        self.assertTrue(mom1 is not None)

        # Fetch params to validate initial values
        self.assertAllClose([1.0, 2.0], self.evaluate(var0))
        self.assertAllClose([3.0, 4.0], self.evaluate(var1))
        # Step 1: rms = 1, mom = 0. So we should see a normal
        # update: v -= grad * learning_rate
        self.evaluate(update)
        # Check the root mean square accumulators.
        self.assertAllCloseAccordingToType(
            np.array([0.901, 0.901]), self.evaluate(rms0))
        self.assertAllCloseAccordingToType(
            np.array([0.90001, 0.90001]), self.evaluate(rms1))
        # Check the momentum accumulators
        self.assertAllCloseAccordingToType(
            np.array([(0.1 * 2.0 / math.sqrt(0.901 + 1e-5)),
                      (0.1 * 2.0 / math.sqrt(0.901 + 1e-5))]),
            self.evaluate(mom0))
        self.assertAllCloseAccordingToType(
            np.array([(0.01 * 2.0 / math.sqrt(0.90001 + 1e-5)),
                      (0.01 * 2.0 / math.sqrt(0.90001 + 1e-5))]),
            self.evaluate(mom1))

        # Check that the parameters.
        self.assertAllCloseAccordingToType(
            np.array([
                1.0 - (0.1 * 2.0 / math.sqrt(0.901 + 1e-5)),
                2.0 - (0.1 * 2.0 / math.sqrt(0.901 + 1e-5))
            ]), self.evaluate(var0))
        self.assertAllCloseAccordingToType(
            np.array([
                3.0 - (0.01 * 2.0 / math.sqrt(0.90001 + 1e-5)),
                4.0 - (0.01 * 2.0 / math.sqrt(0.90001 + 1e-5))
            ]), self.evaluate(var1))

        # Step 2: the root mean square accumulators contain the previous update.
        self.evaluate(update)
        # Check the rms accumulators.
        self.assertAllCloseAccordingToType(
            np.array([0.901 * 0.9 + 0.001, 0.901 * 0.9 + 0.001]),
            self.evaluate(rms0))
        self.assertAllCloseAccordingToType(
            np.array([0.90001 * 0.9 + 1e-5, 0.90001 * 0.9 + 1e-5]),
            self.evaluate(rms1))
        self.assertAllCloseAccordingToType(
            np.array([
                0.5 * (0.1 * 2.0 / math.sqrt(0.901 + 1e-5)) +
                (0.1 * 2.0 / math.sqrt(0.901 * 0.9 + 0.001 + 1e-5)),
                0.5 * (0.1 * 2.0 / math.sqrt(0.901 + 1e-5)) +
                (0.1 * 2.0 / math.sqrt(0.901 * 0.9 + 0.001 + 1e-5))
            ]), self.evaluate(mom0))
        self.assertAllCloseAccordingToType(
            np.array([
                0.5 * (0.01 * 2.0 / math.sqrt(0.90001 + 1e-5)) +
                (0.01 * 2.0 / math.sqrt(0.90001 * 0.9 + 2e-5)),
                0.5 * (0.01 * 2.0 / math.sqrt(0.90001 + 1e-5)) +
                (0.01 * 2.0 / math.sqrt(0.90001 * 0.9 + 2e-5))
            ]), self.evaluate(mom1))

        # Check the parameters.
        self.assertAllCloseAccordingToType(
            np.array([
                1.0 - (0.1 * 2.0 / math.sqrt(0.901 + 1e-5)) -
                (0.5 * (0.1 * 2.0 / math.sqrt(0.901 + 1e-5)) +
                 (0.1 * 2.0 / math.sqrt(0.901 * 0.9 + 0.001 + 1e-5))),
                2.0 - (0.1 * 2.0 / math.sqrt(0.901 + 1e-5)) -
                (0.5 * (0.1 * 2.0 / math.sqrt(0.901 + 1e-5)) +
                 (0.1 * 2.0 / math.sqrt(0.901 * 0.9 + 0.001 + 1e-5)))
            ]), self.evaluate(var0))

        self.assertAllCloseAccordingToType(
            np.array([
                3.0 - (0.01 * 2.0 / math.sqrt(0.90001 + 1e-5)) -
                (0.5 * (0.01 * 2.0 / math.sqrt(0.90001 + 1e-5)) +
                 (0.01 * 2.0 / math.sqrt(0.90001 * 0.9 + 2e-5))),
                4.0 - (0.01 * 2.0 / math.sqrt(0.90001 + 1e-5)) -
                (0.5 * (0.01 * 2.0 / math.sqrt(0.90001 + 1e-5)) +
                 (0.01 * 2.0 / math.sqrt(0.90001 * 0.9 + 2e-5)))
            ]), self.evaluate(var1))
