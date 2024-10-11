# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
r = py_builtins.min_(constant_op.constant(2))
self.assertAllEqual(self.evaluate(r), 2)
with self.assertRaises(ValueError):
    py_builtins.min_(constant_op.constant([[2]]))
r = py_builtins.min_(constant_op.constant([3, 1, 2]))
self.assertAllEqual(self.evaluate(r), 1)
with self.assertRaises(ValueError):
    py_builtins.min_(constant_op.constant([[1, 3], [3, 4]]))
r = py_builtins.min_(
    constant_op.constant(6), constant_op.constant(4),
    constant_op.constant(8))
self.assertAllEqual(self.evaluate(r), 4)
with self.assertRaises(ValueError):
    py_builtins.min_(
        constant_op.constant([6]), constant_op.constant(4),
        constant_op.constant(8))
