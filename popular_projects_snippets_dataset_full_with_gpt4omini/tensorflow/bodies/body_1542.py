# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/proximal_adagrad_test.py
with self.session(), self.test_scope():
    var0 = resource_variable_ops.ResourceVariable([0.0, 0.0])
    var1 = resource_variable_ops.ResourceVariable([0.0, 0.0])
    grads0 = constant_op.constant([0.1, 0.2])
    grads1 = constant_op.constant([0.01, 0.02])
    opt = proximal_adagrad.ProximalAdagradOptimizer(
        3.0,
        initial_accumulator_value=0.1,
        l1_regularization_strength=0.0,
        l2_regularization_strength=0.0)
    update = opt.apply_gradients(zip([grads0, grads1], [var0, var1]))
    self.evaluate(variables.global_variables_initializer())

    self.assertAllClose([0.0, 0.0], self.evaluate(var0))
    self.assertAllClose([0.0, 0.0], self.evaluate(var1))

    # Run 3 steps Proximal Adagrad.
    for _ in range(3):
        update.run()

    self.assertAllClose(
        np.array([-2.60260963, -4.29698515]), self.evaluate(var0))
    self.assertAllClose(
        np.array([-0.28432083, -0.56694895]), self.evaluate(var1))
    opt_vars = opt.variables()
    self.assertStartsWith(opt_vars[0].name, var0._shared_name)
    self.assertStartsWith(opt_vars[1].name, var1._shared_name)
    self.assertEqual(2, len(opt_vars))
