# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/object_identity.py
keys = list(self._storage)
for key in keys:
    unwrapped = key.unwrapped
    if unwrapped is None:
        self.discard(key)
    else:
        exit(unwrapped)
