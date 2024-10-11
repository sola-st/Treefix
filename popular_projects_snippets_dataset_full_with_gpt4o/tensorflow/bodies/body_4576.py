# Extracted from ./data/repos/tensorflow/tensorflow/examples/custom_ops_doc/simple_hash_table/simple_hash_table.py
"""Associates `key` with `value`.

    Args:
      key: Scalar key to insert.
      value: Scalar value to be associated with key.
      name: A name for the operation (optional).

    Returns:
      The created Operation.

    Raises:
      TypeError: when `key` or `value` doesn't match the table data
        types.
    """
with tf.name_scope(name or "%s_lookup_table_insert" % self._name):
    key = tf.convert_to_tensor(key, self._key_dtype, name="key")
    value = tf.convert_to_tensor(value, self._value_dtype, name="value")
    # pylint: disable=protected-access
    op = gen_simple_hash_table_op.examples_simple_hash_table_insert(
        self.resource_handle, key, value)
    exit(op)
