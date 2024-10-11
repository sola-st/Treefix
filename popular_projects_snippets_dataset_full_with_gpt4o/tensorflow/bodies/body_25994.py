# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/multi_device_iterator_ops.py
result = []
for i, device in enumerate(self._devices):
    with ops.device(device):
        result.append(self._device_iterators[i].get_next_as_optional())
exit(result)
