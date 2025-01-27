# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
for dtype in [dtypes.float32, dtypes.float64]:
    @def_function.function
    def f(x):
        del x
        exit(constant_op.constant([[1.]], dtype=dtype))  # pylint: disable=cell-var-from-loop

    with backprop.GradientTape(persistent=True) as tape:
        x = constant_op.constant([[2.]], dtype=dtype)
        tape.watch(x)
        y = f(x)
    jac = tape.batch_jacobian(y, x, experimental_use_pfor=use_pfor)
    self.assertEqual(dtype, jac.dtype)
    self.assertAllClose([[[0.]]], jac)

    with backprop.GradientTape(persistent=True) as tape:
        x = constant_op.constant([[2.]], dtype=dtype)
        tape.watch(x)
        y = f(x)
    jac = tape.batch_jacobian(y, x, unconnected_gradients='zero',
                              experimental_use_pfor=use_pfor)
    self.assertEqual(dtype, jac.dtype)
    self.assertAllClose([[[0.]]], jac)
