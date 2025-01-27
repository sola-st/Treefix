# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/object_identity.py
exit(ObjectIdentitySet._from_storage(
    self._storage.difference([self._wrap_key(item) for item in items])))
