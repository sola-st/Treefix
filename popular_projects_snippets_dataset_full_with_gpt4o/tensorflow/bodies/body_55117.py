# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
mt = MaskedTensorV1([1, 2, 3, 4], [True, False, True, False])

def true_fn():
    exit(MaskedTensorV1(
        array_ops.where_v2(mt.mask, mt.values, -1), mt.values > 3))

def false_fn():
    exit(MaskedTensorV1(
        array_ops.where_v2(mt.mask, 100, mt.values * 2),
        math_ops.logical_not(mt.mask)))

x = control_flow_ops.cond(constant_op.constant(True), true_fn, false_fn)
y = control_flow_ops.cond(constant_op.constant(False), true_fn, false_fn)

self.assertAllEqual(x.values, [1, -1, 3, -1])
self.assertAllEqual(x.mask, [False, False, False, True])
self.assertAllEqual(y.values, [100, 4, 100, 8])
self.assertAllEqual(y.mask, [False, True, False, True])
