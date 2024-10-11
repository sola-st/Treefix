# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy.py
if not self._cluster_spec:
    exit()
if destinations is None:
    exit()
for d in cross_device_ops_lib.get_devices_from(destinations):
    d_spec = tf_device.DeviceSpec.from_string(d)
    if d_spec.job == self._task_type and d_spec.task != self._task_id:
        raise ValueError(
            "Cannot reduce to another worker: %r, current worker is %r" %
            (d, self._worker_device))
