# Extracted from ./data/repos/tensorflow/tensorflow/python/training/proximal_adagrad_test.py
# ProximalAdagradOptimizer is supported only in V1.
with ops.Graph().as_default(), self.cached_session():
    var0 = variables.Variable([1.0, 2.0])
    var1 = variables.Variable([4.0, 3.0])
    grads0 = constant_op.constant([0.1, 0.2])
    grads1 = constant_op.constant([0.01, 0.02])

    opt = proximal_adagrad.ProximalAdagradOptimizer(
        3.0,
        initial_accumulator_value=0.1,
        l1_regularization_strength=0.001,
        l2_regularization_strength=0.0)
    update = opt.apply_gradients(zip([grads0, grads1], [var0, var1]))
    self.evaluate(variables.global_variables_initializer())

    v0_val, v1_val = self.evaluate([var0, var1])
    self.assertAllClose([1.0, 2.0], v0_val)
    self.assertAllClose([4.0, 3.0], v1_val)

    # Run 10 steps Proximal Adagrad
    for _ in range(10):
        update.run()
    v0_val, v1_val = self.evaluate([var0, var1])
    self.assertAllClose(np.array([-6.663634, -9.190331]), v0_val)
    self.assertAllClose(np.array([2.959304, 1.029232]), v1_val)
