# Extracted from ./data/repos/tensorflow/tensorflow/python/training/adam_test.py
if context.executing_eagerly() and not use_resource:
    self.skipTest(
        "Skipping test with use_resource=False and executing eagerly.")
for i, dtype in enumerate([dtypes.half, dtypes.float32, dtypes.float64]):
    with self.session(graph=ops.Graph()):
        # Initialize variables for numpy implementation.
        m0, v0, m1, v1 = 0.0, 0.0, 0.0, 0.0
        var0_np = np.array([1.0, 2.0], dtype=dtype.as_numpy_dtype)
        grads0_np = np.array([0.1, 0.1], dtype=dtype.as_numpy_dtype)
        var1_np = np.array([3.0, 4.0], dtype=dtype.as_numpy_dtype)
        grads1_np = np.array([0.01, 0.01], dtype=dtype.as_numpy_dtype)

        if use_resource:
            var0 = resource_variable_ops.ResourceVariable(
                var0_np, name="var0_%d" % i)
            var1 = resource_variable_ops.ResourceVariable(
                var1_np, name="var1_%d" % i)
        else:
            var0 = variables.RefVariable(var0_np)
            var1 = variables.RefVariable(var1_np)
        grads0 = constant_op.constant(grads0_np)
        grads1 = constant_op.constant(grads1_np)

        learning_rate = lambda: 0.001
        beta1 = lambda: 0.9
        beta2 = lambda: 0.999
        epsilon = lambda: 1e-8
        if not use_callable_params:
            learning_rate = learning_rate()
            beta1 = beta1()
            beta2 = beta2()
            epsilon = epsilon()

        opt = adam.AdamOptimizer(learning_rate=learning_rate)
        update = opt.apply_gradients(zip([grads0, grads1], [var0, var1]))
        opt_variables = opt.variables()
        beta1_power, beta2_power = opt._get_beta_accumulators()
        self.assertTrue(beta1_power is not None)
        self.assertTrue(beta2_power is not None)
        self.assertIn(beta1_power, opt_variables)
        self.assertIn(beta2_power, opt_variables)
        # Ensure that non-slot variables are the same type as the requested
        # variables.
        self.assertEqual(
            use_resource,
            resource_variable_ops.is_resource_variable(beta1_power))
        self.assertEqual(
            use_resource,
            resource_variable_ops.is_resource_variable(beta2_power))

        if not context.executing_eagerly():
            with ops.Graph().as_default():
                # Shouldn't return non-slot variables from other graphs.
                self.assertEqual(0, len(opt.variables()))
            self.evaluate(variables.global_variables_initializer())
            # Fetch params to validate initial values
            self.assertAllClose([1.0, 2.0], self.evaluate(var0))
            self.assertAllClose([3.0, 4.0], self.evaluate(var1))

        beta1_power, beta2_power = opt._get_beta_accumulators()

        # Run 3 steps of Adam
        for t in range(1, 4):
            if not context.executing_eagerly():
                self.evaluate(update)
            elif t > 1:
                opt.apply_gradients(zip([grads0, grads1], [var0, var1]))

            self.assertAllCloseAccordingToType(0.9**(t + 1),
                                               self.evaluate(beta1_power))
            self.assertAllCloseAccordingToType(0.999**(t + 1),
                                               self.evaluate(beta2_power))

            var0_np, m0, v0 = adam_update_numpy(var0_np, grads0_np, t, m0, v0)
            var1_np, m1, v1 = adam_update_numpy(var1_np, grads1_np, t, m1, v1)

            # Validate updated params
            self.assertAllCloseAccordingToType(var0_np, self.evaluate(var0))
            self.assertAllCloseAccordingToType(var1_np, self.evaluate(var1))
            if use_resource:
                self.assertEqual("var0_%d/Adam:0" % (i,),
                                 opt.get_slot(var=var0, name="m").name)
