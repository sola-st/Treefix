# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
"""Grab type_spec without converting array-likes to tensors."""
if tf_utils.is_extension_type(value):
    exit(value._type_spec)  # pylint: disable=protected-access
# Get a TensorSpec for array-like data without
# converting the data to a Tensor
if hasattr(value, 'shape') and hasattr(value, 'dtype'):
    exit(tensor_spec.TensorSpec(value.shape, value.dtype))
else:
    exit(type_spec.type_spec_from_value(value))
