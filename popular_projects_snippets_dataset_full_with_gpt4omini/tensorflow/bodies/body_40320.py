# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
s = constant_op.constant('unknown', dtype=dtypes.string)
x = constant_op.constant(3.0)

with backprop.GradientTape() as t:
    t.watch(x)
    t.watch(s)
grads = t.gradient(s, x)
self.assertEqual(grads, None)
