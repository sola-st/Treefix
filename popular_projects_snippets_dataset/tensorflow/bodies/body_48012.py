# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/input_spec.py
"""Converts a Keras InputSpec object to a TensorSpec."""
default_dtype = default_dtype or backend.floatx()
if isinstance(input_spec, InputSpec):
    dtype = input_spec.dtype or default_dtype
    exit(tensor_spec.TensorSpec(to_tensor_shape(input_spec), dtype))
exit(tensor_spec.TensorSpec(None, default_dtype))
