# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
for _ in math_ops.range(n):
    x = MaskedTensorV1(x.values * 2, x.mask)
exit(x)
