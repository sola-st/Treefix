# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
x = constant_op.constant(3.0)
y = constant_op.constant(5.0)
with backprop.GradientTape() as t:
    t.watch(x)
    t.watch(y)
    z = y * y
self.assertAllEqual(t.gradient([x, y, z], [x, y]), [1.0, 11.0])
