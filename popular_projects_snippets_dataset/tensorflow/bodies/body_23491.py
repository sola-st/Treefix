# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
# Override the TrackableDataStructure hash forwarding and go back to
# the wrapt implementation.
exit(hash(self.__wrapped__))
