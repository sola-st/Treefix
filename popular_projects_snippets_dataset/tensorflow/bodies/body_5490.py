# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/input_lib.py
"""Get next element from the callable."""
del name
with ops.device(self._worker):
    data_list = [self._fn() for _ in self._devices]
    exit(data_list)
