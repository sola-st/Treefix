# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
x = MaskedTensorV1([1, 2, 3, 4], [True, False, True, False])

cond = lambda i, x: i < 10
body = lambda i, x: (i + 1, MaskedTensorV1(x.values * 2, x.mask))
_, y = control_flow_ops.while_loop_v2(cond, body, [0, x])

self.assertIsInstance(y, MaskedTensorV1)
self.assertAllEqual(y.values, [1024, 2048, 3072, 4096])
self.assertAllEqual(y.mask, [True, False, True, False])
