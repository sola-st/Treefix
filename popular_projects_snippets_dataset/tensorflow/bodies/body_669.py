# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/adagrad_da_test.py
for dtype in self.float_types:
    with self.session(), self.test_scope():
        global_step = resource_variable_ops.ResourceVariable(
            0, dtype=dtypes.int64)
        var0 = resource_variable_ops.ResourceVariable([1.0, 2.0], dtype=dtype)
        var1 = resource_variable_ops.ResourceVariable([4.0, 3.0], dtype=dtype)
        grads0 = constant_op.constant([0.1, 0.2], dtype=dtype)
        grads1 = constant_op.constant([0.01, 0.02], dtype=dtype)

        opt = adagrad_da.AdagradDAOptimizer(
            3.0,
            global_step,
            initial_gradient_squared_accumulator_value=0.1,
            l1_regularization_strength=0.001,
            l2_regularization_strength=0.0)
        update = opt.apply_gradients(
            zip([grads0, grads1], [var0, var1]), global_step=global_step)
        self.evaluate(variables.global_variables_initializer())

        self.assertAllCloseAccordingToType([1.0, 2.0], self.evaluate(var0))
        self.assertAllCloseAccordingToType([4.0, 3.0], self.evaluate(var1))

        # Run a step of AdagradDA
        update.run()

        self.assertAllCloseAccordingToType(
            np.array([-0.895489, -1.59555]), self.evaluate(var0))
        self.assertAllCloseAccordingToType(
            np.array([-0.085339, -0.17989]), self.evaluate(var1))
