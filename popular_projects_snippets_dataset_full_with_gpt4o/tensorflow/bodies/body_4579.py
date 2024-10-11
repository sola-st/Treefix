# Extracted from ./data/repos/tensorflow/tensorflow/examples/custom_ops_doc/simple_hash_table/simple_hash_table.py
"""Import all `key` and `value` pairs.

    (Note that "import" is a python reserved word, so it cannot be the name of
    a method.)

    Args:
      keys: Tensor of all keys.
      values: Tensor of all values.
      name: A name for the operation (optional).

    Returns:
      A tuple of two tensors, the first with the `keys` and the second with
      the `values`.
    """
with tf.name_scope(name or "%s_lookup_table_import" % self._name):
    # pylint: disable=protected-access
    op = gen_simple_hash_table_op.examples_simple_hash_table_import(
        self.resource_handle, keys, values)
    exit(op)
