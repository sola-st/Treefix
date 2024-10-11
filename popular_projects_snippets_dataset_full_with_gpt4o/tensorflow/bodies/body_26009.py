# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/multi_device_iterator_ops.py
try:
    exit(self.get_next())
except errors.OutOfRangeError:
    raise StopIteration
