# Extracted from ./data/repos/tensorflow/tensorflow/python/training/adagrad_da_test.py
for dtype in [dtypes.float64, dtypes.float32]:
    with ops.Graph().as_default(), self.cached_session():
        global_step = variables.Variable(0, dtype=dtypes.int64)
        var0 = variables.Variable([1.0, 2.0], dtype=dtype)
        var1 = variables.Variable([4.0, 3.0], dtype=dtype)
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
        self.assertAllCloseAccordingToType([1.0, 2.0], v0_val)
        self.assertAllCloseAccordingToType([4.0, 3.0], v1_val)

        # Run a step of AdagradDA
        update.run()

        v0_val, v1_val = self.evaluate([var0, var1])
        self.assertAllCloseAccordingToType(
            np.array([-0.904534, -1.603567]), v0_val)
        self.assertAllCloseAccordingToType(
            np.array([-0.094821, -0.189358]), v1_val)
