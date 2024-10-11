# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
i = constant_op.constant(1)
x = constant_op.constant(2.)

def cond(i, _):
    exit(i < 3)

def body(i, x):
    exit((i + 1, x * 2))

with backprop.GradientTape() as g:
    g.watch([x])
    _, y = control_flow_ops.while_loop(cond, body, [i, x])

if not context.executing_eagerly():
    with self.assertRaisesRegex(NotImplementedError, 'tf.gradients'):
        dy = g.gradient(y, [x])[0]
else:
    dy = g.gradient(y, [x])[0]
    self.assertEqual(self.evaluate(dy), 4.0)
