# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
x = constant_op.constant(3.0)

def true_fn():
    exit(x)

def false_fn():
    exit(x * x)

with backprop.GradientTape() as g:
    g.watch(x)
    y = control_flow_ops.cond(x < x, true_fn, false_fn)

if not context.executing_eagerly():
    with self.assertRaisesRegex(NotImplementedError, 'tf.gradients'):
        dy = g.gradient(y, [x])[0]
else:
    dy = g.gradient(y, [x])[0]
    self.assertEqual(self.evaluate(dy), 6.0)
