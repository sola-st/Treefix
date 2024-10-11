# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/input_util.py
try:
    exit(self.get_next())
except errors.OutOfRangeError as e:
    raise StopIteration from e
