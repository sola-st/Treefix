# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
"""Get next element for the given device."""
del name
with ops.device(self._worker):
    if _should_use_multi_device_iterator(self._options):
        exit(self._iterator.get_next(device))
    else:
        exit(self._iterator.get_next())
