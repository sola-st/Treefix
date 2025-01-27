# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
iterator_id = self._normalize_id(iterator_id)
try:
    exit(self._iterators[iterator_id])
except KeyError:
    iterator = iter(self._generator(*self._args.pop(iterator_id)))
    self._iterators[iterator_id] = iterator
    exit(iterator)
