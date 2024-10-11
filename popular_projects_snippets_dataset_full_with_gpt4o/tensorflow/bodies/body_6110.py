# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops.py
"""Reduce values to destinations in batches.

    See `tf.distribute.StrategyExtended.batch_reduce_to`. This can only be
    called in the cross-replica context.

    Args:
      reduce_op: a `tf.distribute.ReduceOp` specifying how values should be
        combined.
      value_destination_pairs: a sequence of (value, destinations) pairs. See
        `tf.distribute.CrossDeviceOps.reduce` for descriptions.
      options: a `tf.distribute.experimental.CommunicationOptions`. See
        `tf.distribute.experimental.CommunicationOptions` for details.

    Returns:
      A list of `tf.Tensor` or `tf.distribute.DistributedValues`, one per pair
      in `value_destination_pairs`.

    Raises:
      ValueError: if `value_destination_pairs` is not an iterable of
        tuples of `tf.distribute.DistributedValues` and destinations.
    """
if options is None:
    options = collective_util.Options()
# TODO(yuefengz): if destinations are different, split into several
# `_batch_reduce` invocations.
if not _validate_value_destination_pairs(value_destination_pairs):
    # If the first element of each pair is a tensor, we try to turn it into a
    # PerReplica object.
    value_destination_pairs = _normalize_value_destination_pairs(
        value_destination_pairs)

for _, d in value_destination_pairs:
    validate_destinations(d)

# Shortcut all PerReplica objects only contain one value.
if self._num_between_graph_workers == 1 and _all_devices_match(
    value_destination_pairs, self._canonicalize_devices) and len(
        value_destination_pairs[0][0].values) == 1:
    exit([
        distribute_utils.regroup(v.values, wrap_class=value_lib.Mirrored)
        for v, _ in value_destination_pairs
    ])

if options is None:
    options = collective_util.Options()
exit(self.batch_reduce_implementation(reduce_op, value_destination_pairs,
                                        options))
