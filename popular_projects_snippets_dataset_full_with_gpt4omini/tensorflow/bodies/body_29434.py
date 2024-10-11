# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_nd_ops_test.py
ref = variables.Variable(["qq", "ww", "ee", "rr", "", "", "", ""])
indices = constant_op.constant([[4], [3], [1], [7]])
updates = constant_op.constant(["aa", "dd", "cc", "bb"])
update = state_ops.scatter_nd_update(ref, indices, updates)
self.evaluate(variables.global_variables_initializer())
self.assertAllEqual(
    self.evaluate(update),
    [b"qq", b"cc", b"ee", b"dd", b"aa", b"", b"", b"bb"])
