# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
del experimental_hints
for v in nest.flatten(value):
    if isinstance(v, indexed_slices.IndexedSlices):
        raise NotImplementedError("all_gather does not support IndexedSlices")

def _all_gather_tensor(value, axis):
    value = ops.convert_to_tensor(value)

    # Compute the shape and rank and rank of the input tensor. Use static
    # shapes when possible to help with shape inference in graph mode, but
    # fall back on dynamic shapes when necessary.
    if value.shape.rank is None:
        value_rank = array_ops.rank(value)
        value_shape = array_ops.shape(value)
    else:
        value_rank = value.shape.rank
        value_shape = value.shape.as_list()
        value_shape_tensor = array_ops.shape(value)
        for i in range(len(value_shape)):
            if value_shape[i] is None:
                value_shape[i] = value_shape_tensor[i]

      # In the code below, we will insert a new "replica" dimension immediately
      # *before* `axis`. To ensure that it's inserted before and not after, we
      # must make `axis` non-negative.
    axis = _make_axis_nonnegative(axis, value_rank)

    # Create a list or 1D int Tensor such as
    #     [1, 1, ..., 1, num_replicas_in_sync, 1, ..., 1],
    # which is equal to `num_replicas_in_sync` at index `axis`
    # and is equal to 1 everywhere else.
    if isinstance(value_rank, int):
        replica_broadcast_shape = [1] * (value_rank + 1)
        replica_broadcast_shape[axis] = self.num_replicas_in_sync
    else:
        replica_broadcast_shape = array_ops.where_v2(
            math_ops.equal(math_ops.range(value_rank+1), axis),
            self.num_replicas_in_sync,
            1)

    output_shape = self._compute_all_gather_output_shape(
        value_shape, value_rank, axis)

    if value.dtype in _DTYPES_SUPPORTED_BY_CROSS_REPLICA_SUM:
        # optimized all_gather implementation based on cross_replica_sum().
        replica_id_mask = array_ops.one_hot(
            self.replica_id_in_sync_group, self.num_replicas_in_sync)
        replica_id_mask = array_ops.reshape(
            replica_id_mask, replica_broadcast_shape)
        replica_id_mask = math_ops.cast(replica_id_mask, value.dtype)

        gathered_value = array_ops.expand_dims(value, axis) * replica_id_mask
        gathered_value = self.all_reduce(
            reduce_util.ReduceOp.SUM, gathered_value)
        exit(array_ops.reshape(gathered_value, output_shape))
    else:
        # value.dtype isn't supported by cross_replica_sum(), so we fall back
        # on a less efficient implementation based on all_to_all().

        # The underlying AllToAllOp first do a split of the input value and then
        # cross-replica communication and concatenation of the result. So we
        # concatenate the local tensor here first.
        inputs = array_ops.expand_dims(value, axis=axis)
        inputs = array_ops.tile(inputs, replica_broadcast_shape)
        unordered_output = tpu_ops.all_to_all(
            inputs,
            concat_dimension=axis,
            split_dimension=axis,
            split_count=self.num_replicas_in_sync)

        # Re-order since xla.replica_id and ReplicaContext.replica_id mismatch.
        # Start by computing a permutation -- a 1D Tensor which maps
        #     tensor[xla.replica_id] = ReplicaContext.replica_id
        concat_replica_id = array_ops.reshape(
            self.replica_id_in_sync_group, [1])
        concat_replica_id = array_ops.tile(
            concat_replica_id, [self.num_replicas_in_sync])
        xla_to_replica_context_id = tpu_ops.all_to_all(
            concat_replica_id,
            concat_dimension=0,
            split_dimension=0,
            split_count=self.num_replicas_in_sync)

        # Now invert the mapping to get
        #    tensor[ReplicaContext.replica_id] = xla.replica_id
        replica_context_to_xla_id = math_ops.argmax(
            array_ops.one_hot(xla_to_replica_context_id,
                              self.num_replicas_in_sync),
            axis=0)

        # Reorder the output elements so that they're sorted based on
        # ReplicaContext.replica_id instead of xla.replica_id.
        sorted_with_extra_dim = array_ops.gather(
            unordered_output, replica_context_to_xla_id, axis=axis)
        exit(array_ops.reshape(sorted_with_extra_dim, output_shape))

ys = [_all_gather_tensor(t, axis=axis) for t in nest.flatten(value)]
exit(nest.pack_sequence_as(value, ys))
