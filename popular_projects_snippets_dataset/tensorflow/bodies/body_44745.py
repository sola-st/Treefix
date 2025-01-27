# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
iterable_1 = constant_op.constant([2, 3, 1])
self.assertListEqual(
    list(self.evaluate(py_builtins.sorted_(iterable_1))), [1, 2, 3])
self.assertListEqual(
    list(self.evaluate(py_builtins.sorted_(iterable_1, key=lambda x: -x))),
    [3, 2, 1])
self.assertListEqual(
    list(self.evaluate(py_builtins.sorted_(iterable_1, reverse=True))),
    [3, 2, 1])
self.assertListEqual(
    list(
        self.evaluate(
            py_builtins.sorted_(iterable_1, key=lambda x: -x,
                                reverse=True))), [1, 2, 3])

iterable_2 = constant_op.constant([[4, 3], [2, 1]])
with self.assertRaises(ValueError):
    py_builtins.sorted_(iterable_2)
with self.assertRaises(ValueError):
    py_builtins.sorted_(iterable_2, key=lambda x: -x)
self.assertAllEqual(
    list(
        self.evaluate(
            py_builtins.sorted_(
                iterable_2, key=lambda x: math_ops.reduce_sum(x)))),
    [[2, 1], [4, 3]])
