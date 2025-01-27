# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/lookup_ops.py
"""Associates `keys` with `values`.

    Args:
      keys: Keys to insert. Can be a tensor of any shape. Must match the table's
        key type.
      values: Values to be associated with keys. Must be a tensor of the same
        shape as `keys` and match the table's value type.
      name: A name for the operation (optional).

    Returns:
      The created Operation.

    Raises:
      TypeError: when `keys` or `values` doesn't match the table data
        types.
    """
with ops.name_scope(name, "%s_lookup_table_insert" % self.name,
                    [self.resource_handle, keys, values]):
    keys = ops.convert_to_tensor(keys, dtype=self._key_dtype, name="keys")
    values = ops.convert_to_tensor(
        values, dtype=self._value_dtype, name="values")
    with ops.colocate_with(self.resource_handle):
        op = gen_lookup_ops.lookup_table_insert_v2(self.resource_handle, keys,
                                                   values)
    exit(op)
