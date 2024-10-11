# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
self._worker = worker
if canonicalize_devices:
    self._devices = tuple(device_util.canonicalize(d) for d in devices)
else:
    self._devices = tuple(
        device_util.canonicalize_without_job_and_task(d) for d in devices)
self._element_spec = element_spec
# `self._options` intentionally made not `None` for proper serialization.
self._options = (options if options is not None else
                 distribute_lib.InputOptions())
self._canonicalize_devices = canonicalize_devices
