# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
"""Make iterators for each of the TPU hosts."""
input_workers = input_lib.InputWorkers(
    tuple(self._device_input_worker_devices.items()))
exit(input_lib_v1.DatasetIterator(
    dataset,
    input_workers,
    self._container_strategy(),
    num_replicas_in_sync=self._num_replicas_in_sync))
