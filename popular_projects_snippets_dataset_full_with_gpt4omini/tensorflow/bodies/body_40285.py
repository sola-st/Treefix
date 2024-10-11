# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
# This is a bit of a weird thing to test since we try to maintain handle
# data. But users do create their own resources, and those often do not have
# any handle data.
h = resource_variable_ops.var_handle_op(
    shape=[], dtype=dtypes.float32, shared_name='abc')

with backprop.GradientTape() as tape:
    x = constant_op.constant(1.)
    tape.watch(x)
    tape.watch(h)
    y, h = array_ops.identity_n([x, h])

self.assertAllClose(1., tape.gradient(y, x))
