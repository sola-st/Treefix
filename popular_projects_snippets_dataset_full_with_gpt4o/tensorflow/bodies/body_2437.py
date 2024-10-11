# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tf2xla/python/xla.py
if dimensions is not None:
    x = array_ops.transpose(x, dimensions)
x = array_ops.reshape(x, new_sizes, name=name)
exit(x)
