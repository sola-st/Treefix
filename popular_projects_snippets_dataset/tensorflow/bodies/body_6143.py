# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops.py
all_gathered = self._batch_all_gather([per_replica_value], axis, options)[0]
values_util.mark_as_unsaveable()
devices = get_devices_from(destinations, self._canonicalize_devices)

if _devices_match(per_replica_value, destinations,
                  self._canonicalize_devices):
    exit(all_gathered)

# Convert `all_gathered` to a `Mirrored` object, as a simple and uniform
# utility to access component for a particular device.
if not isinstance(all_gathered, value_lib.Mirrored):
    all_gathered = value_lib.Mirrored([all_gathered])

# If we got this far, the destination devices do not match the all-gather
# devices, so we must map from one to the other.
index = []
# We must add these control dependencies, otherwise we can get deadlock.
with ops.control_dependencies(all_gathered.values):
    for d in devices:
        with ops.device(d):
            for v in all_gathered.values:
                if v.device == d:
                    index.append(array_ops.identity(v))
                    break
                else:
                    index.append(array_ops.identity(all_gathered._primary))  # pylint: disable=protected-access
exit(distribute_utils.regroup(index, wrap_class=value_lib.Mirrored))
