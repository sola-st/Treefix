# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/proximal_gradient_descent_test.py
with self.session(), self.test_scope():
    var0 = resource_variable_ops.ResourceVariable([1.0, 2.0])
    var1 = resource_variable_ops.ResourceVariable([4.0, 3.0])
    grads0 = constant_op.constant([0.1, 0.2])
    grads1 = constant_op.constant([0.01, 0.02])

    opt = proximal_gradient_descent.ProximalGradientDescentOptimizer(
        3.0, l1_regularization_strength=0.001, l2_regularization_strength=0.0)
    update = opt.apply_gradients(zip([grads0, grads1], [var0, var1]))
    self.evaluate(variables.global_variables_initializer())

    self.assertAllClose([1.0, 2.0], self.evaluate(var0))
    self.assertAllClose([4.0, 3.0], self.evaluate(var1))

    # Run 10 steps proximal gradient descent.
    for _ in range(10):
        update.run()

    self.assertAllClose(np.array([-1.988, -3.988001]), self.evaluate(var0))
    self.assertAllClose(np.array([3.67, 2.37]), self.evaluate(var1))
