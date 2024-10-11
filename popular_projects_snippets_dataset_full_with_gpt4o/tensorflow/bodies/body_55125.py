# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
if isinstance(x, MaskedTensorV1):
    exit(x.values * 2)
else:
    exit(MaskedTensorV1(x, x > i))
