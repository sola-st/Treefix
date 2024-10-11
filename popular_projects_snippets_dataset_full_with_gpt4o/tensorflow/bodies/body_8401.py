# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
exit(numpy_dataset.one_host_numpy_dataset(
    numpy_input, numpy_dataset.SingleDevice(self._host_device),
    session))
