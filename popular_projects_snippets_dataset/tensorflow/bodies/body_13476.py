# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/lookup_ops.py
empty_key = ops.convert_to_tensor(
    self._empty_key, dtype=self._key_dtype, name="empty_key")
deleted_key = ops.convert_to_tensor(
    self._deleted_key, dtype=self._key_dtype, name="deleted_key")
if self._is_anonymous:
    table_ref = gen_lookup_ops.anonymous_mutable_dense_hash_table(
        empty_key=empty_key,
        deleted_key=deleted_key,
        value_dtype=self._value_dtype,
        value_shape=self._value_shape,
        initial_num_buckets=self._initial_num_buckets,
        name=self._name)
else:
    # The table must be shared if checkpointing is requested for multi-worker
    # training to work correctly. Use the node name if no shared_name has been
    # explicitly specified.
    use_node_name_sharing = self._checkpoint and self._shared_name is None
    table_ref = gen_lookup_ops.mutable_dense_hash_table_v2(
        empty_key=empty_key,
        deleted_key=deleted_key,
        shared_name=self._shared_name,
        use_node_name_sharing=use_node_name_sharing,
        value_dtype=self._value_dtype,
        value_shape=self._value_shape,
        initial_num_buckets=self._initial_num_buckets,
        name=self._name)
if context.executing_eagerly():
    self._table_name = None
else:
    self._table_name = table_ref.op.name.split("/")[-1]
exit(table_ref)
