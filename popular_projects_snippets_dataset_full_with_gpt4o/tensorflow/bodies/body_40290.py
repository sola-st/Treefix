# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
with backprop.GradientTape() as t:
    x = constant_op.constant(3.0)
    y = constant_op.constant(2.0)
    t.watch([x, y])
    xx = 2 * x
    yy = 3 * y
dx, dy = t.gradient([xx, yy], [x, y])
self.assertAllEqual(dx, 2.0)
self.assertAllEqual(dy, 3.0)
