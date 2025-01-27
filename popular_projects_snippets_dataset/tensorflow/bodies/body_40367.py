# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
with backprop.GradientTape(persistent=True) as g:
    # Using different constant values because constant tensors are
    # cached, leading to a different gradient then what one might expect.
    x1 = constant_op.constant(3.0)
    x2 = constant_op.constant(3.1)
    x3 = constant_op.constant(3.2)
    g.watch(x1)
    g.watch(x2)
    g.watch(x3)
    y = x1 + 2 * x2 + 3 * x3
self.assertEqual(self.evaluate(g.gradient(y, x1)), [1.0])
self.assertEqual(self.evaluate(g.gradient(y, (x1,))), (1.0,))
self.assertEqual(self.evaluate(g.gradient(y, (x1, x2))), (1.0, 2.0))
self.assertEqual(
    self.evaluate(g.gradient(y, [(x1, x2), (x2, x3)])), [(1.0, 2.0),
                                                         (2.0, 3.0)])
self.assertEqual(
    self.evaluate(g.gradient(y, (x1, x2, [x1, x3]))),
    (1.0, 2.0, [1.0, 3.0]))
self.assertEqual(
    self.evaluate(g.gradient(y, [x1, {
        'x2': x2,
        'x3': x3
    }])), [1.0, {
        'x2': 2.0,
        'x3': 3.0
    }])
