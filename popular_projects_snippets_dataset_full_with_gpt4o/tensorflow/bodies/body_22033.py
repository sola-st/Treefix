# Extracted from ./data/repos/tensorflow/tensorflow/python/training/proximal_gradient_descent_test.py
with ops.Graph().as_default(), self.cached_session():
    var0 = variables.Variable([1.0, 2.0])
    var1 = variables.Variable([4.0, 3.0])
    grads0 = constant_op.constant([0.1, 0.2])
    grads1 = constant_op.constant([0.01, 0.02])

    opt = proximal_gradient_descent.ProximalGradientDescentOptimizer(
        3.0, l1_regularization_strength=0.0, l2_regularization_strength=0.0)
    update = opt.apply_gradients(zip([grads0, grads1], [var0, var1]))
    self.evaluate(variables.global_variables_initializer())

    v0_val, v1_val = self.evaluate([var0, var1])
    self.assertAllClose([1.0, 2.0], v0_val)
    self.assertAllClose([4.0, 3.0], v1_val)

    # Run 3 steps Proximal Gradient Descent
    for _ in range(3):
        update.run()

    v0_val, v1_val = self.evaluate([var0, var1])
    self.assertAllClose(np.array([0.1, 0.2]), v0_val)
    self.assertAllClose(np.array([3.91, 2.82]), v1_val)
