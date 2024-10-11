# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
if isinstance(x, ops.Tensor):
    exit(array_ops.placeholder_with_default(x, shape=None))
else:
    exit(x)
