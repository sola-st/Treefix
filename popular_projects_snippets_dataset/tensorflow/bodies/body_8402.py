# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
if not options or options.experimental_fetch_to_device:
    exit(input_lib.InputWorkers(
        tuple(self._device_input_worker_devices.items())))
else:
    exit(input_lib.InputWorkers(
        tuple(self._host_input_worker_devices.items())))
