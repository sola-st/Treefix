# Extracted from ./data/repos/tensorflow/tensorflow/python/training/adadelta_test.py
num_updates = 4  # number of ADADELTA steps to perform
for dtype in [dtypes.half, dtypes.float32]:
    for grad in [0.2, 0.1, 0.01]:
        for lr in [1.0, 0.5, 0.1]:
            var0_init = [1.0, 2.0]
            var1_init = [3.0, 4.0]
            if use_resource:
                var0 = resource_variable_ops.ResourceVariable(
                    var0_init, dtype=dtype)
                var1 = resource_variable_ops.ResourceVariable(
                    var1_init, dtype=dtype)
            else:
                var0 = variables.Variable(var0_init, dtype=dtype)
                var1 = variables.Variable(var1_init, dtype=dtype)

            grads = constant_op.constant([grad, grad], dtype=dtype)

            accum = 0.0
            accum_update = 0.0

            # ADADELTA gradient optimizer
            rho = 0.95
            epsilon = 1e-8
            if use_callable_params:
                adadelta_opt = adadelta.AdadeltaOptimizer(
                    learning_rate=lambda: lr,  # pylint: disable=cell-var-from-loop
                    rho=lambda: rho,  # pylint: disable=cell-var-from-loop
                    epsilon=lambda: epsilon)  # pylint: disable=cell-var-from-loop
            else:
                adadelta_opt = adadelta.AdadeltaOptimizer(
                    learning_rate=lr, rho=rho, epsilon=epsilon)
            if not context.executing_eagerly():
                adadelta_update = adadelta_opt.apply_gradients(
                    zip([grads, grads], [var0, var1]))
                self.evaluate(variables.global_variables_initializer())

                # TODO(lxuechen): This is hard to test in eager mode,
                # since the optimizer is not fully initialized until the first
                # call to `apply_gradients`
                opt_vars = adadelta_opt.variables()
                self.assertStartsWith(opt_vars[0].name, var0._shared_name)
                self.assertStartsWith(opt_vars[1].name, var0._shared_name)
                self.assertStartsWith(opt_vars[2].name, var1._shared_name)
                self.assertStartsWith(opt_vars[3].name, var1._shared_name)
                self.assertEqual(4, len(opt_vars))
                # Assign slots
                slot = [None] * 2
                slot_update = [None] * 2
                self.assertEqual(["accum", "accum_update"],
                                 adadelta_opt.get_slot_names())
                slot[0] = adadelta_opt.get_slot(var0, "accum")
                self.assertEqual(slot[0].get_shape(), var0.get_shape())
                self.assertFalse(slot[0] in variables.trainable_variables())

                slot_update[0] = adadelta_opt.get_slot(var0, "accum_update")
                self.assertEqual(slot_update[0].get_shape(), var0.get_shape())
                self.assertFalse(slot_update[0] in variables.trainable_variables())

                slot[1] = adadelta_opt.get_slot(var1, "accum")
                self.assertEqual(slot[1].get_shape(), var1.get_shape())
                self.assertFalse(slot[1] in variables.trainable_variables())

                slot_update[1] = adadelta_opt.get_slot(var1, "accum_update")
                self.assertEqual(slot_update[1].get_shape(), var1.get_shape())
                self.assertFalse(slot_update[1] in variables.trainable_variables())

            # Fetch params to validate initial values
            self.assertAllClose(var0_init, self.evaluate(var0))
            self.assertAllClose(var1_init, self.evaluate(var1))

            update = [None] * num_updates
            tot_update = 0
            for step in range(num_updates):
                # Run adadelta update for comparison
                if not context.executing_eagerly():
                    self.evaluate(adadelta_update)
                else:
                    adadelta_opt.apply_gradients(zip([grads, grads], [var0, var1]))

                # Perform initial update without previous accum values
                accum = accum * rho + (grad**2) * (1 - rho)
                update[step] = (
                    np.sqrt(accum_update + epsilon) *
                    (1. / np.sqrt(accum + epsilon)) * grad)
                accum_update = (
                    accum_update * rho + (update[step]**2) * (1.0 - rho))
                tot_update += update[step] * lr

                if not context.executing_eagerly():
                    # Check that the accumulators have been updated
                    # TODO(lxuechen): This is hard to test in eager mode
                    for slot_idx in range(2):
                        self.assertAllCloseAccordingToType(
                            np.array([accum, accum], dtype=dtype.as_numpy_dtype()),
                            self.evaluate(slot[slot_idx]),
                            rtol=1e-5)

                        self.assertAllCloseAccordingToType(
                            np.array(
                                [accum_update, accum_update],
                                dtype=dtype.as_numpy_dtype()),
                            self.evaluate(slot_update[slot_idx]),
                            rtol=1e-5)

                    # Check that the parameters have been updated
                    self.assertAllCloseAccordingToType(
                        np.array(
                            [var0_init[0] - tot_update, var0_init[1] - tot_update],
                            dtype=dtype.as_numpy_dtype()),
                        self.evaluate(var0),
                        rtol=1e-5)

                    self.assertAllCloseAccordingToType(
                        np.array(
                            [var1_init[0] - tot_update, var1_init[1] - tot_update],
                            dtype=dtype.as_numpy_dtype()),
                        self.evaluate(var1),
                        rtol=1e-5)
