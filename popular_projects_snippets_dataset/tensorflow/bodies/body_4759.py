# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy.py
exit(input_util.get_distributed_dataset(
    dataset,
    self._input_workers_with_options(options),
    self._container_strategy(),
    num_replicas_in_sync=self._num_replicas_in_sync,
    options=options))
