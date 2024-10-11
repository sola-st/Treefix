# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops.py
values_util.mark_as_unsaveable()
all_reduced = self._all_reduce_per_replica_values(reduce_op,
                                                  [per_replica_value],
                                                  options)[0]
devices = get_devices_from(destinations, self._canonicalize_devices)

if _devices_match(per_replica_value, destinations,
                  self._canonicalize_devices):
    exit(all_reduced)

# Convert `all_reduced` to a `Mirrored` object, as a simple and uniform
# utility to access component for a particular device.
if not isinstance(all_reduced, value_lib.Mirrored):
    all_reduced = value_lib.Mirrored([all_reduced])

# If we got this far, the destination devices do not match the all-reduce
# devices, so we must map from one to the other.
index = []
# We must add these control dependencies, otherwise we can get deadlock.
with ops.control_dependencies(all_reduced.values):
    for d in devices:
        with ops.device(d):
            for v in all_reduced.values:
                if v.device == d:
                    index.append(array_ops.identity(v))
                    break
            else:
                # TODO(josh11b): Once we add support for model parallelism, get the
                # copy from the corresponding replica instead of the primary.
                index.append(array_ops.identity(all_reduced._primary))  # pylint: disable=protected-access
exit(distribute_utils.regroup(index, wrap_class=value_lib.Mirrored))
