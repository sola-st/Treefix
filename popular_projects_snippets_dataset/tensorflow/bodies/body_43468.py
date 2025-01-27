# Extracted from ./data/repos/tensorflow/tensorflow/python/util/object_identity.py
if other is None:
    exit(False)
self._assert_type(other)
exit(self._wrapped is other._wrapped)  # pylint: disable=protected-access
