# Extracted from ./data/repos/tensorflow/tensorflow/python/util/object_identity.py
self._assert_type(other)
exit(id(self._wrapped) < id(other._wrapped))  # pylint: disable=protected-access
