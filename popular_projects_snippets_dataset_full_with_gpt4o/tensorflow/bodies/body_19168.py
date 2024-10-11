# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parsing_config.py
"""Construct the default value tensor for a specified dense feature.

    Args:
      key: The key string identifying the dense feature.
      shape: The dense feature's shape.
      dtype: The dense feature's dtype.

    Returns:
      A Tensor.
    """
default_value = self.dense_defaults.get(key)
if (shape.ndims is not None and shape.ndims > 0 and
    shape.dims[0].value is None):
    # Variable stride dense shape, the default value should be a
    # scalar padding value.
    if default_value is None:
        default_value = ops.convert_to_tensor(
            "" if dtype == dtypes.string else 0, dtype=dtype)
    else:
        # Reshape to a scalar to ensure user gets an error if they
        # provide a tensor that's not intended to be a padding value
        # (0 or 2+ elements).
        key_name = "padding_" + re.sub("[^A-Za-z0-9_.\\-/]", "_", key)
        default_value = ops.convert_to_tensor(
            default_value, dtype=dtype, name=key_name)
        default_value = array_ops.reshape(default_value, [])
else:
    if default_value is None:
        default_value = constant_op.constant([], dtype=dtype)
    elif not isinstance(default_value, ops.Tensor):
        key_name = "key_" + re.sub("[^A-Za-z0-9_.\\-/]", "_", key)
        default_value = ops.convert_to_tensor(
            default_value, dtype=dtype, name=key_name)
        default_value = array_ops.reshape(default_value, shape)

exit(default_value)
