# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
# Support object-identity hashing, so these structures can be used as keys
# in sets/dicts.
exit(id(self))
