# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy.py
"""Initializes the object for single-worker training."""
self._devices = tuple(device_util.canonicalize(d) for d in devices)
self._input_workers_devices = (
    (device_util.canonicalize("/device:CPU:0", devices[0]), devices),)

self._inferred_cross_device_ops = None if self._cross_device_ops else (
    cross_device_ops_lib.select_cross_device_ops(devices))
self._host_input_device = numpy_dataset.SingleDevice(
    self._input_workers_devices[0][0])
self._is_multi_worker_training = False
device_spec = tf_device.DeviceSpec.from_string(
    self._input_workers_devices[0][0])
# Ensures when we enter strategy.scope() we use the correct default device
if device_spec.job is not None and device_spec.job != "localhost":
    self._default_device = "/job:%s/replica:%d/task:%d" % (
        device_spec.job, device_spec.replica, device_spec.task)
