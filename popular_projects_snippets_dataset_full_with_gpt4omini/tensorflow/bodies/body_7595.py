# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2.py
input_workers_devices = self._input_workers_with_options()

# If this DistributedDataset is created outside ClusterCoordinator, i,e,
# outside a tf.function, we don't build its underlying datasets immediately
# until it is passed to ClusterCoordinator.create_per_worker_dataset.
exit(input_util.get_distributed_dataset(
    dataset,
    input_workers_devices,
    self._container_strategy(),
    num_replicas_in_sync=self._num_replicas_in_sync,
    options=options,
    build=ops.inside_function()))  # will be built by ClusterCoordinator
