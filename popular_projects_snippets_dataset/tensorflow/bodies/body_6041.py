# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/one_device_strategy.py
if not options or options.experimental_fetch_to_device:
    exit(input_lib.InputWorkers([(self._input_device, (self._device,))]))
else:
    exit(input_lib.InputWorkers([(self._input_device,
                                    (self._input_device,))]))
