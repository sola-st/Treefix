# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/iterator_ops.py
try:
    exit(self._next_internal())
except errors.OutOfRangeError:
    raise StopIteration
