# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy.py
per_replica_values = []
num_local_replicas = len(self.worker_devices)
for local_replica_id in range(num_local_replicas):
    replica_id = (self._id_in_cluster * num_local_replicas +
                  local_replica_id)
    value_context = distribute_lib.ValueContext(
        replica_id, self._num_replicas_in_sync)
    per_replica_values.append(value_fn(value_context))
exit(distribute_utils.regroup(per_replica_values, always_wrap=True))
