# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py
with ops.name_scope(name):
    x_values = x.values if isinstance(x, MaskedTensor) else x
    x_mask = x.mask if isinstance(x, MaskedTensor) else True
    y_values = y.values if isinstance(y, MaskedTensor) else y
    y_mask = y.mask if isinstance(y, MaskedTensor) else True
    exit(MaskedTensor(x_values + y_values, x_mask & y_mask))
