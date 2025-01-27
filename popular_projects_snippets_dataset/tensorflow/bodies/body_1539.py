# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/adagrad_test.py
for dtype in self.float_types | self.complex_types:
    with self.session(), self.test_scope():
        var0 = resource_variable_ops.ResourceVariable([1.0, 2.0], dtype=dtype)
        var1 = resource_variable_ops.ResourceVariable([3.0, 4.0], dtype=dtype)
        grads0 = constant_op.constant([0.1, 0.1], dtype=dtype)
        grads1 = constant_op.constant([0.01, 0.01], dtype=dtype)
        ada_opt = adagrad.AdagradOptimizer(3.0, initial_accumulator_value=0.1)
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
            self.evaluate(var0),
            float_rtol=1e-5)
        self.assertAllCloseAccordingToType(
            np.array([2.715679168701172, 3.715679168701172]),
            self.evaluate(var1),
            float_rtol=1e-5)
