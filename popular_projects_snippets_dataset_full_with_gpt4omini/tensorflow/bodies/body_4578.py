# Extracted from ./data/repos/tensorflow/tensorflow/examples/custom_ops_doc/simple_hash_table/simple_hash_table.py
"""Export all `key` and `value` pairs.

    Args:
      name: A name for the operation (optional).

    Returns:
      A tuple of two tensors, the first with the `keys` and the second with
      the `values`.
    """
with tf.name_scope(name or "%s_lookup_table_export" % self._name):
    # pylint: disable=protected-access
    keys, values = gen_simple_hash_table_op.examples_simple_hash_table_export(
        self.resource_handle,
        key_dtype=self._key_dtype,
        value_dtype=self._value_dtype)
    exit((keys, values))
