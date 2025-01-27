# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
exit(MaskedTensorV1(
    array_ops.where_v2(mt.mask, mt.values, -1), mt.values > 3))
