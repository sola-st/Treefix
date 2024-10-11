# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops.py
"""Run batch all-reduces."""
logging.log_first_n(
    logging.INFO,
    "batch_all_reduce: %d all-reduces with algorithm = %s, num_packs = %d" %
    (len(dense_values), self._all_reduce_alg, self._num_packs), 10)

destinations = dense_values[0]._devices  # pylint: disable=protected-access
grouped = _group_value_by_device(dense_values)

# device_grad_packs:
# [[(t0_gpu0, None), (t1_gpu0, None)], [(t0_gpu1, None), (t1_gpu1, None)]]
device_grad_packs, tensor_packer = _pack_tensors(grouped, self._num_packs)

# The actual aggregation of the repacked gradients. Note that they are
# sharded among different aggregation trees. So it is important to strike
# the balance on num_splits.
if self._all_reduce_alg == "nccl":
    # TODO(yuefengz): merge this into the all-reduce library.
    reduced = cross_device_utils.aggregate_gradients_using_nccl(
        device_grad_packs)
else:
    # TODO(yuefengz): check that gpu ids in `destinations` are in ascending
    # order.
    reduced = (
        cross_device_utils.aggregate_gradients_using_hierarchical_copy(
            destinations, device_grad_packs))

reduced = _unpack_tensors(reduced, tensor_packer)
exit(_ungroup_and_make_mirrored(reduced, dense_values[0], reduce_op))
