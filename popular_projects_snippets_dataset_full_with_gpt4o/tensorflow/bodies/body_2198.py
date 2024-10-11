# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/ftrl_test.py
"""Test the new FTRL op with support for l2 shrinkage.

    The addition of this parameter which places a constant pressure on weights
    towards the origin causes the gradient descent trajectory to differ. The
    weights will tend to have smaller magnitudes with this parameter set.
    """
for dtype in self.float_types:
    with self.session(), self.test_scope():
        var0 = resource_variable_ops.ResourceVariable([1.0, 2.0], dtype=dtype)
        var1 = resource_variable_ops.ResourceVariable([4.0, 3.0], dtype=dtype)
        grads0 = constant_op.constant([0.1, 0.2], dtype=dtype)
        grads1 = constant_op.constant([0.01, 0.02], dtype=dtype)
        opt = ftrl.FtrlOptimizer(
            3.0,
            initial_accumulator_value=0.1,
            l1_regularization_strength=0.001,
            l2_regularization_strength=2.0,
            l2_shrinkage_regularization_strength=0.1)
        ftrl_update = opt.apply_gradients(zip([grads0, grads1], [var0, var1]))
        self.evaluate(variables.global_variables_initializer())
        # Fetch params to validate initial values
        self.assertAllCloseAccordingToType([1.0, 2.0], self.evaluate(var0))
        self.assertAllCloseAccordingToType([4.0, 3.0], self.evaluate(var1))

        # Run 10 steps FTRL
        for _ in range(10):
            ftrl_update.run()

        # Validate updated params
        self.assertAllCloseAccordingToType(
            np.array([-0.22578996, -0.44345799]),
            self.evaluate(var0),
            rtol=1e-4)
        self.assertAllCloseAccordingToType(
            np.array([-0.14378493, -0.13229476]),
            self.evaluate(var1),
            rtol=1e-4)
