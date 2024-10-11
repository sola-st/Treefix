# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy.py
exit(input_lib_v1.DatasetIterator(
    dataset,
    self._input_workers,
    self._container_strategy(),
    num_replicas_in_sync=self._num_replicas_in_sync))
