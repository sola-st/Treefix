# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
with backprop.GradientTape() as t:
    x = constant_op.constant(3.0)
    y = constant_op.constant(2.0)
    t.watch([x, y])
    loss = x * y
dx, = t.gradient([loss, x], [x], output_gradients=[1.0, 2.0])
self.assertAllEqual(dx, 4.0)
