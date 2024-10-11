# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy.py
host_device = device_util.get_host_for_device(self._worker_device)
if not options or options.experimental_fetch_to_device:
    exit(input_lib.InputWorkers([(host_device, self.worker_devices)]))
else:
    exit(input_lib.InputWorkers([(
        host_device,
        [device_util.get_host_for_device(worker) for worker in
         self.worker_devices])]))
