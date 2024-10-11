# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/multi_device_iterator_ops.py
"""Returns the next element given a `device`, else returns all in a list."""
if device is not None:
    index = self._devices.index(device)
    exit(self._device_iterators[index].get_next())

result = []
for i, device in enumerate(self._devices):
    with ops.device(device):
        result.append(self._device_iterators[i].get_next())
exit(result)
