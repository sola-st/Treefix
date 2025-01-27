# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/adagrad_test.py
for dtype in self.float_types:
    with self.session(), self.test_scope():
        var0 = resource_variable_ops.ResourceVariable([1.0, 2.0], dtype=dtype)
        var1 = resource_variable_ops.ResourceVariable([3.0, 4.0], dtype=dtype)
        grads0 = constant_op.constant([0.1, 0.1], dtype=dtype)
        grads1 = constant_op.constant([0.01, 0.01], dtype=dtype)
        ada_opt = adagrad.AdagradOptimizer(3.0)
        # Apply the optimizer twice.  Both applications will use
        # the same accums.
        ada_update1 = ada_opt.apply_gradients(
            zip([grads0, grads1], [var0, var1]))
        ada_update2 = ada_opt.apply_gradients(
            zip([grads0, grads1], [var0, var1]))
        self.assertEqual(["accumulator"], ada_opt.get_slot_names())
        slot0 = ada_opt.get_slot(var0, "accumulator")
        self.assertEqual(slot0.get_shape(), var0.get_shape())
        slot1 = ada_opt.get_slot(var1, "accumulator")
        self.assertEqual(slot1.get_shape(), var1.get_shape())
        self.evaluate(variables.global_variables_initializer())

        # Fetch params to validate initial values.
        self.assertAllClose([1.0, 2.0], self.evaluate(var0))
        self.assertAllClose([3.0, 4.0], self.evaluate(var1))
        # Mix the first and the second adagrad for 3 steps.
        ada_update1.run()
        ada_update2.run()
        ada_update1.run()
        # Validate updated params (the same as with only 1 Adagrad).
        self.assertAllCloseAccordingToType(
            np.array([-1.6026098728179932, -0.6026098728179932]),
            self.evaluate(var0),
            float_rtol=1e-5)
        self.assertAllCloseAccordingToType(
            np.array([2.715679168701172, 3.715679168701172]),
            self.evaluate(var1),
            float_rtol=1e-5)
