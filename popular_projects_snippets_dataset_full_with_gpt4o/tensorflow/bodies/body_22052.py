# Extracted from ./data/repos/tensorflow/tensorflow/python/training/proximal_adagrad_test.py
# ProximalAdagradOptimizer is supported only in V1.
with ops.Graph().as_default(), self.cached_session():
    var0 = variables.Variable([0.0, 0.0])
    var1 = variables.Variable([0.0, 0.0])
    grads0 = constant_op.constant([0.1, 0.2])
    grads1 = constant_op.constant([0.01, 0.02])
    opt = proximal_adagrad.ProximalAdagradOptimizer(
        3.0,
        initial_accumulator_value=0.1,
        l1_regularization_strength=0.0,
        l2_regularization_strength=0.0)
    update = opt.apply_gradients(zip([grads0, grads1], [var0, var1]))
    self.evaluate(variables.global_variables_initializer())

    v0_val, v1_val = self.evaluate([var0, var1])
    self.assertAllClose([0.0, 0.0], v0_val)
    self.assertAllClose([0.0, 0.0], v1_val)

    # Run 3 steps Proximal Adagrad.
    for _ in range(3):
        update.run()

    v0_val, v1_val = self.evaluate([var0, var1])
    self.assertAllClose(np.array([-2.60260963, -4.29698515]), v0_val)
    self.assertAllClose(np.array([-0.28432083, -0.56694895]), v1_val)
    opt_vars = opt.variables()
    self.assertStartsWith(opt_vars[0].name, var0._shared_name)
    self.assertStartsWith(opt_vars[1].name, var1._shared_name)
    self.assertEqual(2, len(opt_vars))
