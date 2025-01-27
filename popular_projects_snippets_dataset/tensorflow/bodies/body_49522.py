# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/object_identity.py
if not isinstance(other, _ObjectIdentityWrapper):
    raise TypeError("Cannot compare wrapped object with unwrapped object")
