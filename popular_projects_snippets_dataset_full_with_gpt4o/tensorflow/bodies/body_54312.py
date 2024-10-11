# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()
with g.as_default():
    x = constant_op.constant(1)
    y = constant_op.constant(2)
    z = x + y

z.op._update_input(0, y)  # pylint: disable=protected-access
self.assertEqual(list(z.op.inputs), [y, y])
self.assertEqual(x.consumers(), [])
self.assertEqual(y.consumers(), [z.op, z.op])
with session.Session(graph=g) as sess:
    self.assertEqual(self.evaluate(z), 4)

z.op._update_input(0, x)  # pylint: disable=protected-access
self.assertEqual(list(z.op.inputs), [x, y])
self.assertEqual(x.consumers(), [z.op])
self.assertEqual(y.consumers(), [z.op])
with session.Session(graph=g) as sess:
    self.assertEqual(self.evaluate(z), 3)

z.op._update_input(1, y)  # pylint: disable=protected-access
self.assertEqual(list(z.op.inputs), [x, y])
self.assertEqual(x.consumers(), [z.op])
self.assertEqual(y.consumers(), [z.op])
with session.Session(graph=g) as sess:
    self.assertEqual(self.evaluate(z), 3)
