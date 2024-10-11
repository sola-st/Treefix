# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/lookup_ops.py
"""Looks up `keys` in a table, outputs the corresponding values.

    The `default_value` is used for keys not present in the table.

    Args:
      keys: Keys to look up. Can be a tensor of any shape. Must match the
        table's key_dtype.
      dynamic_default_values: The values to use if a key is missing in the
        table. If None (by default), the `table.default_value` will be used.
        Shape of `dynamic_default_values` must be same with
        `table.default_value` or the lookup result tensor.
        In the latter case, each key will have a different default value.

        For example:

          ```python
          keys = [0, 1, 3]
          dynamic_default_values = [[1, 3, 4], [2, 3, 9], [8, 3, 0]]

          # The key '0' will use [1, 3, 4] as default value.
          # The key '1' will use [2, 3, 9] as default value.
          # The key '3' will use [8, 3, 0] as default value.
          ```

      name: A name for the operation (optional).

    Returns:
      A tensor containing the values in the same shape as `keys` using the
        table's value type.

    Raises:
      TypeError: when `keys` do not match the table data types.
    """
with ops.name_scope(name, "%s_lookup_table_find" % self.name,
                    (self.resource_handle, keys, self._default_value)):
    keys = ops.convert_to_tensor(keys, dtype=self._key_dtype, name="keys")
    with ops.colocate_with(self.resource_handle):
        values = gen_lookup_ops.lookup_table_find_v2(
            self.resource_handle, keys, dynamic_default_values
            if dynamic_default_values is not None else self._default_value)
exit(values)
