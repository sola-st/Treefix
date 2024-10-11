# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
self.assertEqual(py_builtins.float_(10), 10.0)
self.assertEqual(py_builtins.float_('10.0'), 10.0)
with self.cached_session() as sess:
    t = py_builtins.float_(constant_op.constant(1, dtype=dtypes.int64))
    self.assertEqual(self.evaluate(t), 1.0)
    st = py_builtins.float_(constant_op.constant('1.0'))
    self.assertEqual(self.evaluate(st), 1.0)
