# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops.py
"""Implements CrossDeviceOps.all_reduce."""
# TODO(b/122840926): reuse this method in _batch_all_reduce.
flat_values = nest.flatten(value)

# If NCCL launches can't be ordered (self._limited_nccl == True), we only
# use NCCL when batch_size > 1, hoping that there's only one batched
# all-reduce, which is the gradient aggregation in optimizer. For TF 2.x,
# NCCL launches are always ordered.
if (self._limited_nccl and options.implementation
    == collective_util.CommunicationImplementation.NCCL and
    len(flat_values) == 1):
    options = options.merge(
        collective_util.Options(
            implementation=collective_util.CommunicationImplementation.RING))

launcher = self._launchers[replica_id]
dense_values, dense_indices, sparse_values, sparse_indices = (
    cross_device_utils.split_by_sparsity(flat_values))
dense_results = []
sparse_results = []

if dense_values:
    # Reverse the lists so that there's better chance that values follows
    # the order in which they are calculated (e.g. when they're gradients), so
    # as to overlap calculation with communication. However, this may not be
    # optimal for cases like gradients of complicated non-sequential models.
    #
    # Note that we reverse the list before packing so that the first pack
    # won't be too small, since it's more likely for first few packs to have
    # long queuing time due to concurrent intense computation.
    #
    # TODO(b/147393503): explore solutions for optimal ordering.
    dense_values.reverse()
    packs = cross_device_utils.group_by_size(dense_values,
                                             options.bytes_per_pack)

    if not context.executing_eagerly() and replica_id == 0:
        logging.info(
            "Collective all_reduce tensors: %d all_reduces, num_devices = %d, "
            "group_size = %d, implementation = %s, num_packs = %d",
            len(dense_values), len(self._launchers), self._group_size,
            options.implementation, len(packs))

    dense_results = launcher.batch_all_reduce(packs, options)
    if reduce_op == reduce_util.ReduceOp.MEAN:
        for i, v in enumerate(dense_results):
            with ops.device(self._devices[replica_id]):
                dense_results[i] = v / self._group_size
    dense_results.reverse()

if sparse_values:
    if not context.executing_eagerly() and replica_id == 0:
        logging.info(
            "Collective all_reduce IndexedSlices: %d all_reduces, num_devices ="
            "%d, group_size = %d, implementation = %s", len(sparse_values),
            len(self._launchers), self._group_size, options.implementation)

    for indexed_slice in sparse_values:
        sparse_results.append(
            launcher.all_reduce_indexed_slices(indexed_slice, options))

    if reduce_op == reduce_util.ReduceOp.MEAN:
        for i, v in enumerate(sparse_results):
            with ops.device(self._devices[replica_id]):
                sparse_results[i] = indexed_slices.IndexedSlices(
                    values=sparse_results[i].values / self._group_size,
                    indices=sparse_results[i].indices,
                    dense_shape=sparse_results[i].dense_shape)

flat_results = cross_device_utils.stitch_values(
    ((dense_results, dense_indices), (sparse_results, sparse_indices)))
exit(nest.pack_sequence_as(value, flat_results))
