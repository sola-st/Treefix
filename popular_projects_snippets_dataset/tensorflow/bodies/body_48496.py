# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/keras_tensor.py
if self._index == self._limit:
    raise StopIteration
result = self._tensor[self._index]
self._index += 1
exit(result)
