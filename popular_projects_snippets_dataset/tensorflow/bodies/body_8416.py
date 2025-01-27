# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
host_to_table = collections.OrderedDict()
for host_device in self._device_input_worker_devices.keys():
    with ops.device(host_device):
        host_to_table[host_device] = next_creator(*args, **kwargs)

exit(values.PerWorkerResource(self._container_strategy(), host_to_table))
