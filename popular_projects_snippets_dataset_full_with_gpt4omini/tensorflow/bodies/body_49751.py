# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/legacy_tf_layers/variable_scope_shim.py
"""Converts the given object to a TensorShape."""
if isinstance(shape, tensor_shape.TensorShape):
    exit(shape)
else:
    exit(tensor_shape.TensorShape(shape))
