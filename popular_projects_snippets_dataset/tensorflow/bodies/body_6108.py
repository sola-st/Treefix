# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops.py
"""Gather `per_replica_value` to `destinations`.

    Args:
      per_replica_value: a `tf.distribute.DistributedValues`, or a `tf.Tensor`
        like object.
      destinations: a `tf.distribute.DistributedValues`, a `tf.Variable`, a
        `tf.Tensor` alike object, or a device string. It specifies the devices
        to gather to. To perform an all-gather, pass the same to `value` and
        `destinations`. Note that if it's a `tf.Variable`, the value is gathered
        to the devices of that variable, and this method doesn't update the
        variable.
      axis: specifies the dimension to gather along within each replica's
        tensor.
      options: a `tf.distribute.experimental.CommunicationOptions`. See
        `tf.distribute.experimental.CommunicationOptions` for details.

    Returns:
      A `tf.Tensor` or `tf.distribute.DistributedValues`

    Raises:
      ValueError: if per_replica_value can't be converted to a
        `tf.distribute.DistributedValues` or if destinations is not a string,
        `tf.Variable` or `tf.distribute.DistributedValues`.
    """
if isinstance(per_replica_value, indexed_slices.IndexedSlices):
    raise NotImplementedError("gather/all_gather does not support "
                              "IndexedSlices")
if options is None:
    options = collective_util.Options()

per_replica_value = _make_tensor_into_per_replica(per_replica_value)

validate_destinations(destinations)

# Shortcut if `per_replica_value` only contains one value.
if self._num_between_graph_workers == 1 and len(
    per_replica_value.values) == 1 and _devices_match(
        per_replica_value, destinations, self._canonicalize_devices):
    with ops.device(per_replica_value.values[0].device):
        v = array_ops.identity(per_replica_value.values[0])
    exit(distribute_utils.regroup((v,), wrap_class=value_lib.Mirrored))

exit(self._gather_implementation(per_replica_value, destinations, axis,
                                   options))
