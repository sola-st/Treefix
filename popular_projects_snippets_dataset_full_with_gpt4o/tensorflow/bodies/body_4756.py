# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy.py
if not options or options.experimental_fetch_to_device:
    exit(input_lib.InputWorkers(
        [(self._worker_device, self._compute_devices)]))
else:
    exit(input_lib.InputWorkers(
        [(self._worker_device,
          (self._worker_device,) * len(self._compute_devices))]))
