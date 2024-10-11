# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py
if y is None:
    exit(x)
y_values = y.values if isinstance(y, MaskedTensor) else y
y_mask = y.mask if isinstance(y, MaskedTensor) else True
exit(MaskedTensor(x.values + y_values, x.mask & y_mask))
