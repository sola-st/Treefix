# Extracted from ./data/repos/tensorflow/tensorflow/python/training/adagrad_test.py
with ops.Graph().as_default():
    for dtype in [dtypes.half, dtypes.float32, dtypes.float64]:
        with self.cached_session():
            var0 = variables.Variable([1.0, 2.0], dtype=dtype)
            var1 = variables.Variable([3.0, 4.0], dtype=dtype)
            grads0 = constant_op.constant([0.1, 0.1], dtype=dtype)
            grads1 = constant_op.constant([0.01, 0.01], dtype=dtype)
            ada_opt = adagrad.AdagradOptimizer(
                constant_op.constant(3.0), initial_accumulator_value=0.1)
            ada_update = ada_opt.apply_gradients(
                zip([grads0, grads1], [var0, var1]))
            self.evaluate(variables.global_variables_initializer())
            # Fetch params to validate initial values
            self.assertAllClose([1.0, 2.0], self.evaluate(var0))
            self.assertAllClose([3.0, 4.0], self.evaluate(var1))
            # Run 3 steps of adagrad
            for _ in range(3):
                ada_update.run()
            # Validate updated params
            self.assertAllCloseAccordingToType(
                np.array([-1.6026098728179932, -0.6026098728179932]),
                self.evaluate(var0))
            self.assertAllCloseAccordingToType(
                np.array([2.715679168701172, 3.715679168701172]),
                self.evaluate(var1))
