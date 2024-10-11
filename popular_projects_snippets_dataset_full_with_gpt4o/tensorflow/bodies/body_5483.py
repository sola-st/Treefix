# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/input_lib.py
"""Make appropriate iterator on the dataset."""
with ops.device(self._worker):
    if self._options is not None:
        self._iterator = multi_device_iterator_ops.MultiDeviceIterator(
            self._dataset,
            self._devices,
            max_buffer_size=self._options.experimental_per_replica_buffer_size,
            prefetch_buffer_size=self._options
            .experimental_per_replica_buffer_size)
    else:
        self._iterator = multi_device_iterator_ops.MultiDeviceIterator(
            self._dataset,
            self._devices,
        )
