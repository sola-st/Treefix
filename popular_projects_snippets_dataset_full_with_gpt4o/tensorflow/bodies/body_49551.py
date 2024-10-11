# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/object_identity.py
exit(self._storage.intersection([self._wrap_key(item) for item in items]))
