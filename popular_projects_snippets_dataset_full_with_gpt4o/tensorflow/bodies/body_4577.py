# Extracted from ./data/repos/tensorflow/tensorflow/examples/custom_ops_doc/simple_hash_table/simple_hash_table.py
"""Remove `key`.

    Args:
      key: Scalar key to remove.
      name: A name for the operation (optional).

    Returns:
      The created Operation.

    Raises:
      TypeError: when `key` doesn't match the table data type.
    """
with tf.name_scope(name or "%s_lookup_table_remove" % self._name):
    key = tf.convert_to_tensor(key, self._key_dtype, name="key")

    # For remove, just the key is used by the kernel; no value is used.
    # But the kernel is specifc to key_dtype and value_dtype
    # (i.e. it uses a <key_dtype, value_dtype> template).
    # So value_dtype is passed in explicitly. (While
    # key_dtype is specificed implicitly by the dtype of key.)

    # pylint: disable=protected-access
    op = gen_simple_hash_table_op.examples_simple_hash_table_remove(
        self.resource_handle, key, value_dtype=self._value_dtype)
    exit(op)
