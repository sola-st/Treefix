# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops.py
gathered_values = []
with self._lock, ops.name_scope("allgather"):
    for per_replica in per_replica_values:
        outputs = []
        for i in range(len(self._devices)):
            outputs.append(self._launchers[i].all_gather(
                per_replica.values[i], axis, options))
        gathered_values.append(outputs)
exit(gathered_values)
