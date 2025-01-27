# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/lookup_ops.py
if self._is_anonymous:
    if self._default_value.get_shape().ndims == 0:
        table_ref = gen_lookup_ops.anonymous_mutable_hash_table(
            key_dtype=self._key_dtype,
            value_dtype=self._value_dtype,
            name=self._name)
    else:
        table_ref = gen_lookup_ops.anonymous_mutable_hash_table_of_tensors(
            key_dtype=self._key_dtype,
            value_dtype=self._value_dtype,
            value_shape=self._default_value.get_shape(),
            name=self._name)
else:
    # The table must be shared if checkpointing is requested for multi-worker
    # training to work correctly. Use the node name if no shared_name has been
    # explicitly specified.
    use_node_name_sharing = self._checkpoint and self._shared_name is None
    if self._default_value.get_shape().ndims == 0:
        table_ref = gen_lookup_ops.mutable_hash_table_v2(
            shared_name=self._shared_name,
            use_node_name_sharing=use_node_name_sharing,
            key_dtype=self._key_dtype,
            value_dtype=self._value_dtype,
            name=self._name)
    else:
        table_ref = gen_lookup_ops.mutable_hash_table_of_tensors_v2(
            shared_name=self._shared_name,
            use_node_name_sharing=use_node_name_sharing,
            key_dtype=self._key_dtype,
            value_dtype=self._value_dtype,
            value_shape=self._default_value.get_shape(),
            name=self._name)

if context.executing_eagerly():
    self._table_name = None
else:
    self._table_name = table_ref.op.name.split("/")[-1]
exit(table_ref)
