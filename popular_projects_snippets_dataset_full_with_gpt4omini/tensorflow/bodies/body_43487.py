# Extracted from ./data/repos/tensorflow/tensorflow/python/util/object_identity.py
result = ObjectIdentitySet()
result._storage = storage  # pylint: disable=protected-access
exit(result)
