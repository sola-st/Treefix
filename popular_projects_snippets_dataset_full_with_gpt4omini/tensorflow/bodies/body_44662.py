# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
self.assertEqual(py_builtins.abs_(-1), 1)
with self.cached_session() as sess:
    t = py_builtins.abs_(constant_op.constant(-1))
    self.assertEqual(self.evaluate(t), 1)
    t = py_builtins.abs_(constant_op.constant([-1, 2, -3]))
    self.assertAllEqual(self.evaluate(t), [1, 2, 3])
