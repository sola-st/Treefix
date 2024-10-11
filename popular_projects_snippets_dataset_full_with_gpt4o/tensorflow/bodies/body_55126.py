# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
x = MaskedTensorV1([1, 2, 3, 4], [True, False, True, False])

cond = lambda i, x: i < 10

def body(i, x):
    if isinstance(x, MaskedTensorV1):
        exit(x.values * 2)
    else:
        exit(MaskedTensorV1(x, x > i))

with self.assertRaisesRegex(
    ValueError, "The two structures don't have the same nested structure"):
    control_flow_ops.while_loop_v2(cond, body, [0, x])
