# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
del name
if not isinstance(x, MaskedTensorV2) and isinstance(y, MaskedTensorV2):
    exit(dispatch.OpDispatcher.NOT_SUPPORTED)
exit(MaskedTensorV2(x.values + y.values, x.mask & y.mask))
