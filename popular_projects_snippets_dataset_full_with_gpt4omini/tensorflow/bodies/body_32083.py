# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/reduce_join_op_test.py
foobar = constant_op.constant(["foobar"])
# Old names: keep_dims and reduction_indices
output = string_ops.reduce_join(
    ["foo", "bar"], reduction_indices=0, keep_dims=True)
self.assertAllEqual(foobar, output)
# New names keepdims and axis.
output = string_ops.reduce_join(["foo", "bar"], axis=0, keepdims=True)
self.assertAllEqual(foobar, output)
