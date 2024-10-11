# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type.py
if isinstance(value, ops.Tensor):
    # Note: we intentionally exclude `value.name` from the `TensorSpec`.
    exit(tensor_spec.TensorSpec(value.shape, value.dtype))
if hasattr(value, '_type_spec'):
    exit(value._type_spec)  # pylint: disable=protected-access
exit(value)
