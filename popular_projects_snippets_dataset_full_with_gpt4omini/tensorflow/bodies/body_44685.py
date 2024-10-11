# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
with self.cached_session() as sess:
    r = py_builtins.range_(constant_op.constant(3))
    self.assertAllEqual(self.evaluate(r), [0, 1, 2])
    r = py_builtins.range_(1, constant_op.constant(3))
    self.assertAllEqual(self.evaluate(r), [1, 2])
    r = py_builtins.range_(2, 0, constant_op.constant(-1))
    self.assertAllEqual(self.evaluate(r), [2, 1])
