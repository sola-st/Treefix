# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/lookup_ops.py
"""Removes `keys` and its associated values from the table.

    If a key is not present in the table, it is silently ignored.

    Args:
      keys: Keys to remove. Can be a tensor of any shape. Must match the table's
        key type.
      name: A name for the operation (optional).

    Returns:
      The created Operation.

    Raises:
      TypeError: when `keys` do not match the table data types.
    """
if keys.dtype != self._key_dtype:
    raise TypeError(f"Dtype of argument `keys` must be {self._key_dtype}, "
                    f"received: {keys.dtype}")

with ops.name_scope(name, "%s_lookup_table_remove" % self.name,
                    (self.resource_handle, keys, self._default_value)):
    op = gen_lookup_ops.lookup_table_remove_v2(self.resource_handle, keys)

exit(op)
