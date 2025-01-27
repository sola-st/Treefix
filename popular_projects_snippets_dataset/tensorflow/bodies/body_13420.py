# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/lookup_ops.py
"""Returns tensors of all keys and values in the table.

    Args:
      name: A name for the operation (optional).

    Returns:
      A pair of tensors with the first tensor containing all keys and the
        second tensors containing all values in the table.
    """
with ops.name_scope(name, "%s_Export" % self.name, [self.resource_handle]):
    exported_keys, exported_values = gen_lookup_ops.lookup_table_export_v2(
        self.resource_handle, self._key_dtype, self._value_dtype)

exported_values.set_shape(exported_keys.get_shape().concatenate(
    self._value_shape))
exit((exported_keys, exported_values))
