# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
x_values = x.values if isinstance(x, MaskedTensorV1) else x
y_values = y.values if isinstance(y, MaskedTensorV1) else y
x_mask = x.mask if isinstance(x, MaskedTensorV1) else True
y_mask = y.mask if isinstance(y, MaskedTensorV1) else True
exit(MaskedTensorV1(x_values + y_values, x_mask & y_mask))
