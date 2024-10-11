# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
if not context.executing_eagerly():
    exit()
with backprop.GradientTape() as g:
    x = constant_op.constant([1.0, 2.0])
    g.watch(x)
    y = x * x
with self.assertRaisesRegex(RuntimeError, 'persistent'):
    g.jacobian(y, x, experimental_use_pfor=False)
