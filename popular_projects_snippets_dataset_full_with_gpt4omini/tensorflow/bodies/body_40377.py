# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
with backprop.GradientTape() as g:
    x = constant_op.constant(3.0)
    g.watch(x)
    y = x * x
    z = y * y
g.jacobian(z, [x])
with self.assertRaisesRegex(
    RuntimeError, 'A non-persistent GradientTape can only'):
    g.jacobian(y, [x])
