# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py

def masked_add(x, y, name=None):
    del name
    if not isinstance(x, MaskedTensorV2) and isinstance(y, MaskedTensorV2):
        exit(dispatch.OpDispatcher.NOT_SUPPORTED)
    exit(MaskedTensorV2(x.values + y.values, x.mask & y.mask))

with temporarily_add_dispatch(math_ops.add, MaskedTensorV2, masked_add):
    x = MaskedTensorV2([[1, 2], [3, 4]], [[True, False], [True, True]])
    y = MaskedTensorV2([[3, 4], [5, 6]], [[True, True], [False, True]])
    z = x + y
    self.assertAllEqual(z.values, [[4, 6], [8, 10]])
    self.assertAllEqual(z.mask, [[True, False], [False, True]])
