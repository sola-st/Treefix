# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/one_device_strategy.py
exit(numpy_dataset.one_host_numpy_dataset(
    numpy_input, numpy_dataset.SingleDevice(self._input_device), session))
