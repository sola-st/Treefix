# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
exit(MaskedTensorV1(
    array_ops.where_v2(mt.mask, 100, mt.values * 2),
    math_ops.logical_not(mt.mask)))
