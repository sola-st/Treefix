# Extracted from ./data/repos/tensorflow/tensorflow/python/training/rmsprop_test.py
with context.eager_mode():
    for dtype in [dtypes.half, dtypes.float32]:
        var0 = resource_variable_ops.ResourceVariable([1.0, 2.0], dtype=dtype)
        var1 = resource_variable_ops.ResourceVariable([3.0, 4.0], dtype=dtype)
        grads0 = constant_op.constant([0.1, 0.1], dtype=dtype)
        grads1 = constant_op.constant([0.01, 0.01], dtype=dtype)

        learning_rate = lambda: 2.0
        decay = lambda: 0.9
        momentum = lambda: 0.0
        epsilon = lambda: 1.0
        opt = rmsprop.RMSPropOptimizer(learning_rate, decay, momentum, epsilon)

        # Fetch params to validate initial values
        self.assertAllClose([1.0, 2.0], self.evaluate(var0))
        self.assertAllClose([3.0, 4.0], self.evaluate(var1))
        # Step 1: the rms accumulators where 1. So we should see a normal
        # update: v -= grad * learning_rate
        opt.apply_gradients(zip([grads0, grads1], [var0, var1]))
        # Check the parameters.
        self.assertAllCloseAccordingToType(
            np.array([
                1.0 - (0.1 * 2.0 / math.sqrt(0.901 + 1.0)),
                2.0 - (0.1 * 2.0 / math.sqrt(0.901 + 1.0))
            ]), self.evaluate(var0))
        self.assertAllCloseAccordingToType(
            np.array([
                3.0 - (0.01 * 2.0 / math.sqrt(0.90001 + 1.0)),
                4.0 - (0.01 * 2.0 / math.sqrt(0.90001 + 1.0))
            ]), self.evaluate(var1))
        # Step 2: the root mean square accumulators contain the previous update.
        opt.apply_gradients(zip([grads0, grads1], [var0, var1]))
        # Check the parameters.
        self.assertAllCloseAccordingToType(
            np.array([
                1.0 - (0.1 * 2.0 / math.sqrt(0.901 + 1.0)) -
                (0.1 * 2.0 / math.sqrt(0.901 * 0.9 + 0.001 + 1.0)),
                2.0 - (0.1 * 2.0 / math.sqrt(0.901 + 1.0)) -
                (0.1 * 2.0 / math.sqrt(0.901 * 0.9 + 0.001 + 1.0))
            ]), self.evaluate(var0))
        self.assertAllCloseAccordingToType(
            np.array([
                3.0 - (0.01 * 2.0 / math.sqrt(0.90001 + 1.0)) -
                (0.01 * 2.0 / math.sqrt(0.90001 * 0.9 + 1e-5 + 1.0)),
                4.0 - (0.01 * 2.0 / math.sqrt(0.90001 + 1.0)) -
                (0.01 * 2.0 / math.sqrt(0.90001 * 0.9 + 1e-5 + 1.0))
            ]), self.evaluate(var1))
