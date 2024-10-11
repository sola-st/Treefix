# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/lookup_ops.py
"""Constructs a table initializer object based on keys and values tensors.

    Args:
      keys: The tensor for the keys.
      values: The tensor for the values.
      key_dtype: The `keys` data type. Used when `keys` is a python array.
      value_dtype: The `values` data type. Used when `values` is a python array.
      name: A name for the operation (optional).
    """
if (not context.executing_eagerly() and
    ops.get_default_graph()._get_control_flow_context() is not None):  # pylint: disable=protected-access
    with ops.init_scope():
        self._keys = ops.convert_to_tensor(keys, dtype=key_dtype, name="keys")
        self._values = ops.convert_to_tensor(
            values, dtype=value_dtype, name="values")
else:
    self._keys = ops.convert_to_tensor(keys, dtype=key_dtype, name="keys")
    self._values = ops.convert_to_tensor(
        values, dtype=value_dtype, name="values")
self._name = name if name is not None else "key_value_init"
if context.executing_eagerly():
    # Ensure a unique name when eager execution is enabled to avoid spurious
    # sharing issues.
    # TODO(rohanj): Use context.anonymous_name() instead.
    self._name += str(ops.uid())

super(KeyValueTensorInitializer, self).__init__(self._keys.dtype,
                                                self._values.dtype)
