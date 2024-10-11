# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/object_identity.py
self._storage = set(self._wrap_key(obj) for obj in list(*args))
