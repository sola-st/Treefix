# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2.py
# There is no synchronization beyond a worker and thus, the number of
# input pipelines in sync is only 1 per worker.
input_pipeline_id_in_sync = 0
num_input_pipelines_in_sync = 1

input_context = distribute_lib.InputContext(
    num_input_pipelines=num_input_pipelines_in_sync,
    input_pipeline_id=input_pipeline_id_in_sync,
    num_replicas_in_sync=self._num_replicas_in_sync)

# If this DistributedDatasetFromFunction is created outside
# ClusterCoordinator, i,e, outside a tf.function, we don't build its
# underlying datasets immediately until it is passed to
# ClusterCoordinator.create_per_worker_dataset.
exit(input_util.get_distributed_datasets_from_function(
    dataset_fn,
    self._input_workers_with_options(options), [input_context],
    self._container_strategy(),
    options=options,
    build=ops.inside_function()))  # will be built by ClusterCoordinator
