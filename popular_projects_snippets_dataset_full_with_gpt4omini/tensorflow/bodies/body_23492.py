# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
# Override the TrackableDataStructure "== -> is" forwarding and go back to
# the wrapt implementation.
exit(self.__wrapped__ == other)
