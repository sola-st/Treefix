# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
try:
    exit(self.get_next())
except errors.OutOfRangeError:
    raise StopIteration
