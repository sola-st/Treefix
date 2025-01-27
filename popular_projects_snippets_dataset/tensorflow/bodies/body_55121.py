# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
x = MaskedTensorV2([1, 2, 3, 4], [True, False, True, False])
y = MaskedTensorV2([5, 6, 7, 8], [False, True, True, False])
x = extension_type.pack(x)
y = extension_type.pack(y)

x_2 = control_flow_ops.cond(
    constant_op.constant(True), lambda: x, lambda: y)
y_2 = control_flow_ops.cond(
    constant_op.constant(False), lambda: x, lambda: y)

self.assertAllEqual(x.values, x_2.values)
self.assertAllEqual(x.mask, x_2.mask)
self.assertAllEqual(y.values, y_2.values)
self.assertAllEqual(y.mask, y_2.mask)

a = MaskedTensorV2([1, 2, 3, 4], [True, False, True, False])
b = extension_type.pack(a)
b = control_flow_ops.cond(
    constant_op.constant(True), lambda: array_ops.size(a.mask),
    lambda: array_ops.size(a.values))
self.assertAllEqual(b, 4)

# Note: the following example would fail (with `Retval[0] does not have a
# value`) if `ExtensionType.__getattr__` cached the results of unpacking
# the value.  See the comment in `ExtensionType.__getattr__` for details.
c = MaskedTensorV2([1, 2, 3, 4], [True, False, True, False])
c = extension_type.pack(c)
d = control_flow_ops.cond(
    constant_op.constant(False), lambda: array_ops.size(c.mask),
    lambda: array_ops.size(c.values))
self.assertAllEqual(d, 4)
