# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/lookup_ops.py
"""Looks up `keys` in a table, outputs the corresponding values.

    The `default_value` is used for keys not present in the table.

    Args:
      keys: Keys to look up. Can be a tensor of any shape. Must match the
        table's key_dtype.
      name: A name for the operation (optional).

    Returns:
      A tensor containing the values in the same shape as `keys` using the
        table's value type.

    Raises:
      TypeError: when `keys` do not match the table data types.
    """
with ops.name_scope(name, "%s_lookup_table_find" % self.name,
                    [self.resource_handle, keys]):
    keys = ops.convert_to_tensor(keys, dtype=self._key_dtype, name="keys")
    with ops.colocate_with(self.resource_handle):
        values = gen_lookup_ops.lookup_table_find_v2(self.resource_handle, keys,
                                                     self._default_value)

exit(values)
