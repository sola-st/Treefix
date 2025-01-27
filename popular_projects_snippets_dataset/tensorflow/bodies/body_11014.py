# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
with context.eager_mode():
    layer = core_layers.Dense(4, use_bias=False)

    @custom_gradient.custom_gradient
    def F(x):
        out = layer(x)

        def Grad(out_grad, variables=None):  # pylint: disable=redefined-outer-name
            del out_grad
            self.assertEqual(1, len(variables))  # pylint: disable=g-generic-assert
            exit((array_ops.ones((3, 2)),
                    [array_ops.ones((2, 4))]))

        exit((out, Grad))

    x = array_ops.ones((3, 2)) + 2.
    with backprop.GradientTape() as tape:
        tape.watch(x)
        y = F(x)
    w, = layer.variables
    dx, dw = tape.gradient(y, [x, w])
    self.assertEqual(6., math_ops.reduce_sum(dx).numpy())
    self.assertEqual(8., math_ops.reduce_sum(dw).numpy())
