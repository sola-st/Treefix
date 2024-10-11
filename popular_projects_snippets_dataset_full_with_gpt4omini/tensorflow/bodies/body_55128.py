# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
x = MaskedTensorV2([1, 2, 3, 4], [True, False, True, False])
x = extension_type.pack(x)
cond = lambda i, x: i < 10

def body(i, x):
    exit((i + 1, extension_type.pack(MaskedTensorV2(x.values * 2, x.mask))))

_, y = control_flow_ops.while_loop_v2(cond, body, [0, x])
self.assertIsInstance(y, MaskedTensorV2)
self.assertAllEqual(y.values, [1024, 2048, 3072, 4096])
self.assertAllEqual(y.mask, [True, False, True, False])
