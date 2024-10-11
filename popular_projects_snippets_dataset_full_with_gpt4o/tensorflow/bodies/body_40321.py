# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
s = constant_op.constant('unknown', dtype=dtypes.string)

with backprop.GradientTape() as t:
    t.watch(s)
grads = t.gradient(s, s)
self.assertEqual(grads, None)
