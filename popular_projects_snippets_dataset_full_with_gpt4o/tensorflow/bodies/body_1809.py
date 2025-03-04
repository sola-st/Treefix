# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/rmsprop_test.py
for dtype in self.float_types | self.complex_types:
    for centered in [False, True]:
        with self.session(), self.test_scope():
            # Initialize variables for numpy implementation.
            var0_np = np.array([1.0, 2.0], dtype=dtype)
            grads0_np = np.array([0.1, 0.1], dtype=dtype)
            var1_np = np.array([3.0, 4.0], dtype=dtype)
            grads1_np = np.array([0.01, 0.01], dtype=dtype)
            mg0_np = np.array([0.0, 0.0], dtype=dtype)
            mg1_np = np.array([0.0, 0.0], dtype=dtype)
            rms0_np = np.array([1.0, 1.0], dtype=dtype)
            rms1_np = np.array([1.0, 1.0], dtype=dtype)
            mom0_np = np.array([0.0, 0.0], dtype=dtype)
            mom1_np = np.array([0.0, 0.0], dtype=dtype)

            var0 = resource_variable_ops.ResourceVariable(var0_np)
            var1 = resource_variable_ops.ResourceVariable(var1_np)
            grads0 = constant_op.constant(grads0_np)
            grads1 = constant_op.constant(grads1_np)
            learning_rate = 3.0
            rms_opt = rmsprop.RMSPropOptimizer(learning_rate, centered=centered)
            rms_update = rms_opt.apply_gradients(
                zip([grads0, grads1], [var0, var1]))
            self.evaluate(variables.global_variables_initializer())

            mg0 = rms_opt.get_slot(var0, "mg")
            self.assertEqual(mg0 is not None, centered)
            mg1 = rms_opt.get_slot(var1, "mg")
            self.assertEqual(mg1 is not None, centered)
            rms0 = rms_opt.get_slot(var0, "rms")
            self.assertIsNotNone(rms0)
            rms1 = rms_opt.get_slot(var1, "rms")
            self.assertIsNotNone(rms1)
            mom0 = rms_opt.get_slot(var0, "momentum")
            self.assertIsNotNone(mom0)
            mom1 = rms_opt.get_slot(var1, "momentum")
            self.assertIsNotNone(mom1)

            # Fetch params to validate initial values
            self.assertAllClose([1.0, 2.0], self.evaluate(var0))
            self.assertAllClose([3.0, 4.0], self.evaluate(var1))

            # Run 3 steps of RMSProp
            for _ in range(3):
                self.evaluate(rms_update)

                var0_np, mg0_np, rms0_np, mom0_np = self._rmsprop_update_numpy(
                    var0_np,
                    grads0_np,
                    mg0_np,
                    rms0_np,
                    mom0_np,
                    learning_rate,
                    centered=centered)
                var1_np, mg1_np, rms1_np, mom1_np = self._rmsprop_update_numpy(
                    var1_np,
                    grads1_np,
                    mg1_np,
                    rms1_np,
                    mom1_np,
                    learning_rate,
                    centered=centered)

                # Validate updated params
                if centered:
                    self.assertAllCloseAccordingToType(mg0_np, self.evaluate(mg0))
                    self.assertAllCloseAccordingToType(mg1_np, self.evaluate(mg1))
                self.assertAllCloseAccordingToType(rms0_np, self.evaluate(rms0))
                self.assertAllCloseAccordingToType(rms1_np, self.evaluate(rms1))
                self.assertAllCloseAccordingToType(mom0_np, self.evaluate(mom0))
                self.assertAllCloseAccordingToType(mom1_np, self.evaluate(mom1))
                self.assertAllCloseAccordingToType(var0_np, self.evaluate(var0))
                self.assertAllCloseAccordingToType(var1_np, self.evaluate(var1))
