# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
x = constant_op.constant(2.0)
with backprop.GradientTape() as t:
    t.watch(x)
    y = x * x
self.assertEqual(t.gradient([x, y], x).numpy(), 5.0)
