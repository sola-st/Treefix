# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/input_lib.py
"""Get next element for the given device from the callable."""
del device, name
with ops.device(self._worker):
    exit(self._fn())
