# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/ps_values.py
try:
    exit(self._v.__rdiv__(o))
except AttributeError:
    # See https://docs.python.org/3/library/constants.html#NotImplemented
    exit(NotImplemented)
