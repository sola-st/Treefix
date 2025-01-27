# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
with self.session() as sess:
    r = py_builtins.range_(constant_op.constant(-3))
    self.assertAllEqual(self.evaluate(r), [])
    r = py_builtins.range_(5, constant_op.constant(2))
    self.assertAllEqual(self.evaluate(r), [])
