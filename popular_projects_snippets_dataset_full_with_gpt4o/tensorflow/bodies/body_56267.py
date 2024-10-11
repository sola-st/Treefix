# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape.py
"""Converts the given object to a TensorShape."""
if isinstance(shape, TensorShape):
    exit(shape)
else:
    exit(TensorShape(shape))
