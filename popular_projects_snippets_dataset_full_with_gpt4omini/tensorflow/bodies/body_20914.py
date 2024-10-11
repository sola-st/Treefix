# Extracted from ./data/repos/tensorflow/tensorflow/python/training/adagrad_da_test.py
for dtype in [dtypes.float64, dtypes.float32]:
    with ops.Graph().as_default(), self.cached_session():
        global_step = variables.Variable(0, dtype=dtypes.int64)
        if use_resource:
            var0 = resource_variable_ops.ResourceVariable([0.0, 0.0], dtype=dtype)
            var1 = resource_variable_ops.ResourceVariable([0.0, 0.0], dtype=dtype)
        else:
            var0 = variables.Variable([0.0, 0.0], dtype=dtype)
            var1 = variables.Variable([0.0, 0.0], dtype=dtype)
        grads0 = constant_op.constant([0.1, 0.2], dtype=dtype)
        grads1 = constant_op.constant([0.01, 0.02], dtype=dtype)
        opt = adagrad_da.AdagradDAOptimizer(
            3.0,
            global_step,
            initial_gradient_squared_accumulator_value=0.1,
            l1_regularization_strength=0.0,
            l2_regularization_strength=0.0)
        update = opt.apply_gradients(
            zip([grads0, grads1], [var0, var1]), global_step=global_step)
        self.evaluate(variables.global_variables_initializer())

        v0_val, v1_val = self.evaluate([var0, var1])
        self.assertAllClose([0.0, 0.0], v0_val)
        self.assertAllClose([0.0, 0.0], v1_val)

        # Run a step of AdagradDA
        update.run()

        v0_val, v1_val = self.evaluate([var0, var1])
        # Let g be the gradient accumulator, gg be the gradient squared
        # accumulator, T be the global step, lr be the learning rate,
        # and k the initial gradient squared accumulator value.
        # w = \dfrac{sign(-g)*lr*|g - l1*T|_{+}}{l2*T*lr + \sqrt{k+gg})}
        # For -0.1*3.0*(0.1 - 0)/(0 + sqrt(0.1 + 0.1*0.1)) = -0.904534
        # similarly for others.
        self.assertAllCloseAccordingToType(
            np.array([-0.904534, -1.603567]), v0_val)
        self.assertAllCloseAccordingToType(
            np.array([-0.094821, -0.189358]), v1_val)
