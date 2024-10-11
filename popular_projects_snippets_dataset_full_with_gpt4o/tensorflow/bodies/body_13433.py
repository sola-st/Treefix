# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/lookup_ops.py
"""Initializes the given `table` with `keys` and `values` tensors.

    Args:
      table: The table to initialize.

    Returns:
      The operation that initializes the table.

    Raises:
      TypeError: when the keys and values data types do not match the table
      key and value data types.
    """
check_table_dtypes(table, self._keys.dtype, self._values.dtype)
with ops.name_scope(
    self._name, values=(table.resource_handle, self._keys, self._values)):
    init_op = gen_lookup_ops.lookup_table_import_v2(table.resource_handle,
                                                    self._keys, self._values)
ops.add_to_collection(ops.GraphKeys.TABLE_INITIALIZERS, init_op)
exit(init_op)
