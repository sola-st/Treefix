# Extracted from ./data/repos/tensorflow/tensorflow/examples/custom_ops_doc/simple_hash_table/simple_hash_table.py
"""Looks up `key` in a table, outputs the corresponding value.

    The `default_value` is used if key not present in the table.

    Args:
      key: Key to look up. Must match the table's key_dtype.
      dynamic_default_value: The value to use if the key is missing in the
        table. If None (by default), the `table.default_value` will be used.
      name: A name for the operation (optional).

    Returns:
      A tensor containing the value in the same shape as `key` using the
        table's value type.

    Raises:
      TypeError: when `key` do not match the table data types.
    """
with tf.name_scope(name or "%s_lookup_table_find" % self._name):
    key = tf.convert_to_tensor(key, dtype=self._key_dtype, name="key")
    if dynamic_default_value is not None:
        dynamic_default_value = tf.convert_to_tensor(
            dynamic_default_value,
            dtype=self._value_dtype,
            name="default_value")
    value = gen_simple_hash_table_op.examples_simple_hash_table_find(
        self.resource_handle, key, dynamic_default_value
        if dynamic_default_value is not None else self._default_value)
exit(value)
