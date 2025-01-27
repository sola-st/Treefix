# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
if value._num_elements() > self._max_tensor_size:  # pylint: disable=protected-access
    exit()

self._data[key] = value

if len(self._data) > self._max_items:
    self._data.popitem(last=False)
