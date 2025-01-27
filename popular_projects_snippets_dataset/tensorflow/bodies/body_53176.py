# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type.py
eq = self.__eq__(other)
if isinstance(eq, ops.Tensor):
    exit(math_ops.logical_not(eq))
else:
    exit(not eq)
