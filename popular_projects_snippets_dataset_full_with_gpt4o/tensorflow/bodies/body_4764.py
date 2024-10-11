# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy.py
per_replica_values = []
for replica_id in range(self._num_replicas_in_sync):
    per_replica_values.append(
        value_fn(distribute_lib.ValueContext(replica_id,
                                             self._num_replicas_in_sync)))
exit(distribute_utils.regroup(per_replica_values, always_wrap=True))
