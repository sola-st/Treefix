# Extracted from ./data/repos/tensorflow/tensorflow/python/training/adagrad_test.py
with ops.Graph().as_default():
    for dtype in [dtypes.half, dtypes.float32, dtypes.float64]:
        with self.cached_session():
            shape = [1, 6]
            var0 = variables.Variable(
                [[
                    0.00872496, -0.106952, 0.110467, 0.226505, -0.0147257,
                    -0.0105945
                ]],
                dtype=dtype)
            grads0 = indexed_slices.IndexedSlices(
                constant_op.constant(
                    [[
                        -5.91278e-05, 5.31673e-05, -2.5779e-06, 4.29153e-05,
                        -8.4877e-05, -9.48906e-05
                    ]],
                    shape=shape,
                    dtype=dtype),
                constant_op.constant([0]),
                constant_op.constant(shape))
            ada_opt = adagrad.AdagradOptimizer(1.0, initial_accumulator_value=0.1)
            ada_update = ada_opt.apply_gradients(zip([grads0], [var0]))
            self.assertEqual(["accumulator"], ada_opt.get_slot_names())
            slot0 = ada_opt.get_slot(var0, "accumulator")
            init = variables.global_variables_initializer()
            for _ in range(100):
                init.run()
                ada_update.run()
                self.assertAllCloseAccordingToType(
                    np.array([[0.1, 0.1, 0.1, 0.1, 0.1, 0.1]]),
                    self.evaluate(slot0))
                self.assertAllCloseAccordingToType(
                    np.array([[
                        0.00891194, -0.10712013, 0.11047515, 0.22636929, -0.0144573,
                        -0.01029443
                    ]]), self.evaluate(var0))
