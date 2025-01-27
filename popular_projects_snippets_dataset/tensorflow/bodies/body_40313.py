# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
x = constant_op.constant(3.0)
with backprop.GradientTape() as t:
    t.watch(x)
    y = x
self.assertEqual(t.gradient(y, x).numpy(), 1.0)
