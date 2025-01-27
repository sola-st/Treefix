# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
device_scope = device_util.canonicalize(self._worker, device_util.current())
host_device = device_util.get_host_for_device(device_scope)
# source_device while creating iterator governs the worker device in
# iterator spec.
worker = host_device
specs.append(
    multi_device_iterator_ops.MultiDeviceIteratorSpec(
        self._devices, worker, element_spec=self._element_spec))
