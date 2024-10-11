# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
"""Make appropriate iterator on the dataset."""
if not self._worker:
    raise ValueError("Worker device must be specified when creating an "
                     "owned iterator.")
if _should_use_multi_device_iterator(self._options):
    self._create_owned_multi_device_iterator()
else:
    with ops.device(self._worker):
        self._iterator = iter(self._dataset)
