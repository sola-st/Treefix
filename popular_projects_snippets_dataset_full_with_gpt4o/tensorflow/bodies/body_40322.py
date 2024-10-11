# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
x = constant_op.constant(3.0)
y = constant_op.constant(5.0)
s = constant_op.constant('unknown', dtype=dtypes.string)

with backprop.GradientTape() as t:
    t.watch(x)
    t.watch(y)
    t.watch(s)
    z = y * y
grads = t.gradient([x, y, z, s], [x, y, s])
self.assertAllEqual(grads[:2], [1.0, 11.0])
self.assertEqual(grads[2], None)
