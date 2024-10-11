# Extracted from ./data/repos/tensorflow/tensorflow/python/training/momentum_test.py
for i, dtype in enumerate([dtypes.half, dtypes.float32, dtypes.float64]):
    if use_resource:
        var0 = resource_variable_ops.ResourceVariable([1.0, 2.0],
                                                      dtype=dtype,
                                                      name="var0_%d" % i)
        var1 = resource_variable_ops.ResourceVariable([3.0, 4.0],
                                                      dtype=dtype,
                                                      name="var1_%d" % i)
    else:
        var0 = variables.Variable([1.0, 2.0], dtype=dtype)
        var1 = variables.Variable([3.0, 4.0], dtype=dtype)
    grads0 = constant_op.constant([0.1, 0.1], dtype=dtype)
    grads1 = constant_op.constant([0.01, 0.01], dtype=dtype)
    learning_rate = lambda: 2.0
    momentum = lambda: 0.9
    if not use_callable_params:
        learning_rate = learning_rate()
        momentum = momentum()
    mom_opt = momentum_lib.MomentumOptimizer(
        learning_rate=learning_rate, momentum=momentum)
    mom_update = mom_opt.apply_gradients(zip([grads0, grads1], [var0, var1]))

    if not context.executing_eagerly():
        self.evaluate(variables.global_variables_initializer())
        # Fetch params to validate initial values
        self.assertAllClose([1.0, 2.0], self.evaluate(var0))
        self.assertAllClose([3.0, 4.0], self.evaluate(var1))

    # Check we have slots
    self.assertEqual(["momentum"], mom_opt.get_slot_names())
    slot0 = mom_opt.get_slot(var0, "momentum")
    self.assertEqual(slot0.get_shape(), var0.get_shape())
    slot1 = mom_opt.get_slot(var1, "momentum")
    self.assertEqual(slot1.get_shape(), var1.get_shape())
    if not context.executing_eagerly():
        self.assertFalse(slot0 in variables.trainable_variables())
        self.assertFalse(slot1 in variables.trainable_variables())

    # Step 1: the momentum accumulators where 0. So we should see a normal
    # update: v -= grad * learning_rate
    if not context.executing_eagerly():
        self.evaluate(mom_update)
    # Check that the momentum accumulators have been updated.
    self.assertAllCloseAccordingToType(
        np.array([0.1, 0.1]), self.evaluate(slot0))
    self.assertAllCloseAccordingToType(
        np.array([0.01, 0.01]), self.evaluate(slot1))
    # Check that the parameters have been updated.
    self.assertAllCloseAccordingToType(
        np.array([1.0 - (0.1 * 2.0), 2.0 - (0.1 * 2.0)]), self.evaluate(var0))
    self.assertAllCloseAccordingToType(
        np.array([3.0 - (0.01 * 2.0), 4.0 - (0.01 * 2.0)]),
        self.evaluate(var1))
    # Step 2: the momentum accumulators contain the previous update.
    if context.executing_eagerly():
        mom_opt.apply_gradients(zip([grads0, grads1], [var0, var1]))
    else:
        self.evaluate(mom_update)
    # Check that the momentum accumulators have been updated.
    self.assertAllCloseAccordingToType(
        np.array([(0.9 * 0.1 + 0.1), (0.9 * 0.1 + 0.1)]),
        self.evaluate(slot0))
    self.assertAllCloseAccordingToType(
        np.array([(0.9 * 0.01 + 0.01), (0.9 * 0.01 + 0.01)]),
        self.evaluate(slot1))
    # Check that the parameters have been updated.
    self.assertAllCloseAccordingToType(
        np.array([
            1.0 - (0.1 * 2.0) - ((0.9 * 0.1 + 0.1) * 2.0),
            2.0 - (0.1 * 2.0) - ((0.9 * 0.1 + 0.1) * 2.0)
        ]), self.evaluate(var0))
    self.assertAllCloseAccordingToType(
        np.array([
            2.98 - ((0.9 * 0.01 + 0.01) * 2.0),
            3.98 - ((0.9 * 0.01 + 0.01) * 2.0)
        ]), self.evaluate(var1))
