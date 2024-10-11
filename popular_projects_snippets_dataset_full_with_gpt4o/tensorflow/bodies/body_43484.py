# Extracted from ./data/repos/tensorflow/tensorflow/python/util/object_identity.py
# Iterate, discarding old weak refs
exit(len(list(self._storage)))
