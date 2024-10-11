# Extracted from ./data/repos/tensorflow/tensorflow/python/training/momentum_test.py
for dtype in [dtypes.half, dtypes.float32, dtypes.float64]:
    # train.MomentumOptimizer is V1 only API.
    with ops.Graph().as_default(), self.cached_session():
        var0 = variables.Variable(array_ops.zeros([4, 2], dtype=dtype))
        var1 = variables.Variable(constant_op.constant(1.0, dtype, [4, 2]))
        grads0 = indexed_slices.IndexedSlices(
            constant_op.constant([[.1, .1]], dtype=dtype),
            constant_op.constant([1]), constant_op.constant([4, 2]))
        grads1 = indexed_slices.IndexedSlices(
            constant_op.constant([[.01, .01], [.01, .01]], dtype=dtype),
            constant_op.constant([2, 3]), constant_op.constant([4, 2]))
        mom_opt = momentum_lib.MomentumOptimizer(
            learning_rate=2.0, momentum=0.9)
        mom_update = mom_opt.apply_gradients(
            zip([grads0, grads1], [var0, var1]))
        self.evaluate(variables.global_variables_initializer())

        # Check we have slots
        self.assertEqual(["momentum"], mom_opt.get_slot_names())
        slot0 = mom_opt.get_slot(var0, "momentum")
        self.assertEqual(slot0.get_shape(), var0.get_shape())
        slot1 = mom_opt.get_slot(var1, "momentum")
        self.assertEqual(slot1.get_shape(), var1.get_shape())

        # Fetch params to validate initial values
        self.assertAllClose([0, 0], self.evaluate(var0)[0])
        self.assertAllClose([0, 0], self.evaluate(var0)[1])
        self.assertAllClose([1, 1], self.evaluate(var1)[2])

        # Step 1: the momentum accumulators are 0. So we should see a normal
        # update: v -= grad * learning_rate
        mom_update.run()
        # Check that the momentum accumulators have been updated.
        self.assertAllCloseAccordingToType(
            np.array([0, 0]),
            self.evaluate(slot0)[0])
        self.assertAllCloseAccordingToType(
            np.array([.1, .1]),
            self.evaluate(slot0)[1])
        self.assertAllCloseAccordingToType(
            np.array([.01, .01]),
            self.evaluate(slot1)[2])
        # Check that the parameters have been updated.
        self.assertAllCloseAccordingToType(
            np.array([0, 0]),
            self.evaluate(var0)[0])
        self.assertAllCloseAccordingToType(
            np.array([-(0.1 * 2.0), -(0.1 * 2.0)]),
            self.evaluate(var0)[1])
        self.assertAllCloseAccordingToType(
            np.array([1.0 - (0.01 * 2.0), 1.0 - (0.01 * 2.0)]),
            self.evaluate(var1)[2])
        # Step 2: the momentum accumulators contain the previous update.
        mom_update.run()
        # Check that the momentum accumulators have been updated.
        self.assertAllClose(np.array([0, 0]), self.evaluate(slot0)[0])
        self.assertAllCloseAccordingToType(
            np.array([(0.9 * 0.1 + 0.1), (0.9 * 0.1 + 0.1)]),
            self.evaluate(slot0)[1])
        self.assertAllCloseAccordingToType(
            np.array([(0.9 * 0.01 + 0.01), (0.9 * 0.01 + 0.01)]),
            self.evaluate(slot1)[2])
        # Check that the parameters have been updated.
        self.assertAllClose(np.array([0, 0]), self.evaluate(var0)[0])
        self.assertAllCloseAccordingToType(
            np.array([
                -(0.1 * 2.0) - ((0.9 * 0.1 + 0.1) * 2.0),
                -(0.1 * 2.0) - ((0.9 * 0.1 + 0.1) * 2.0)
            ]),
            self.evaluate(var0)[1])
        self.assertAllCloseAccordingToType(
            np.array([
                0.98 - ((0.9 * 0.01 + 0.01) * 2.0),
                0.98 - ((0.9 * 0.01 + 0.01) * 2.0)
            ]),
            self.evaluate(var1)[2])
