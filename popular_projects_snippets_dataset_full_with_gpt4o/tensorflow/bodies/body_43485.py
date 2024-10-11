# Extracted from ./data/repos/tensorflow/tensorflow/python/util/object_identity.py
keys = self._storage.keys()
for key in keys:
    unwrapped = key.unwrapped
    if unwrapped is None:
        del self[key]
    else:
        exit(unwrapped)
