# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
# If the worker devices are already canonicalized, canonicalizing again
# would have no impact.
# For strategies running on remote workers such as PS Strategy, the device
# scope will be derived from current worker, if used under init_scope().
device_scope = device_util.canonicalize(self._worker,
                                        device_util.current())
host_device = device_util.get_host_for_device(device_scope)
with ops.device(device_scope):
    if self._options is not None:
        self._iterator = multi_device_iterator_ops.OwnedMultiDeviceIterator(
            self._dataset,
            self._devices,
            source_device=host_device,
            max_buffer_size=self._options
            .experimental_per_replica_buffer_size,
            prefetch_buffer_size=self._options
            .experimental_per_replica_buffer_size)
    else:
        self._iterator = multi_device_iterator_ops.OwnedMultiDeviceIterator(
            self._dataset, self._devices, source_device=host_device)
