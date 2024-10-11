# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
try:
    exit(self._get_as_operand().__rmatmul__(o))
except AttributeError:
    # See https://docs.python.org/3/library/constants.html#NotImplemented
    exit(NotImplemented)
