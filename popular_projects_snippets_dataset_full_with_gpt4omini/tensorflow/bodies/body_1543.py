# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/proximal_adagrad_test.py
with self.session(), self.test_scope():
    var0 = resource_variable_ops.ResourceVariable([1.0, 2.0])
    var1 = resource_variable_ops.ResourceVariable([4.0, 3.0])
    grads0 = constant_op.constant([0.1, 0.2])
    grads1 = constant_op.constant([0.01, 0.02])

    opt = proximal_adagrad.ProximalAdagradOptimizer(
        3.0,
        initial_accumulator_value=0.1,
        l1_regularization_strength=0.0,
        l2_regularization_strength=0.0)
    update = opt.apply_gradients(zip([grads0, grads1], [var0, var1]))
    self.evaluate(variables.global_variables_initializer())

    self.assertAllClose([1.0, 2.0], self.evaluate(var0))
    self.assertAllClose([4.0, 3.0], self.evaluate(var1))

    # Run 3 steps Proximal Adagrad.
    for _ in range(3):
        update.run()
    self.assertAllClose(np.array([-1.60261, -2.296985]), self.evaluate(var0))
    self.assertAllClose(np.array([3.715679, 2.433051]), self.evaluate(var1))
