# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
if mt.values[3] > 3:
    exit(MaskedTensorV1(
        array_ops.where_v2(mt.mask, mt.values, -1), mt.values > 3))
else:
    exit(MaskedTensorV1(
        array_ops.where_v2(mt.mask, 100, mt.values * 2), not mt.mask))
