# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/autocast_variable.py
try:
    exit(self.read_value().__div__(o))
except AttributeError:
    # See https://docs.python.org/3/library/constants.html#NotImplemented
    exit(NotImplemented)
