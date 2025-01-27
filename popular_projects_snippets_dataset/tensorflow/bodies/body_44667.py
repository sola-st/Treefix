# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
self.assertEqual(py_builtins.int_(10.0), 10)
self.assertEqual(py_builtins.int_('11', 2), 3)
with self.cached_session() as sess:
    t = py_builtins.int_(constant_op.constant(1, dtype=dtypes.float64))
    self.assertEqual(self.evaluate(t), 1)
    st = py_builtins.int_(constant_op.constant('1'))
    self.assertEqual(self.evaluate(st), 1)
    st = py_builtins.int_(constant_op.constant('1'), 10)
    self.assertEqual(self.evaluate(st), 1)
