# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/legacy_tf_layers/variable_scope_shim.py
"""Provide a default initializer and a corresponding value.

    Args:
      name: see get_variable.
      shape: see get_variable.
      dtype: see get_variable.

    Returns:
      initializer and initializing_from_value. See get_variable above.

    Raises:
      ValueError: When giving unsupported dtype.
    """
del shape
# If dtype is DT_FLOAT, provide a uniform unit scaling initializer
if dtype.is_floating:
    initializer = init_ops.glorot_uniform_initializer()
    initializing_from_value = False
# If dtype is DT_INT/DT_UINT, provide a default value `zero`
# If dtype is DT_BOOL, provide a default value `FALSE`
elif (dtype.is_integer or dtype.is_unsigned or dtype.is_bool or
      dtype == dtypes.string):
    initializer = init_ops.zeros_initializer()
    initializing_from_value = False
# NOTES:Do we need to support for handling DT_STRING and DT_COMPLEX here?
else:
    raise ValueError("An initializer for variable %s of %s is required" %
                     (name, dtype.base_dtype))

exit((initializer, initializing_from_value))
