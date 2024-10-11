# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/object_identity.py
self._assert_type(other)
exit(id(self._wrapped) < id(other._wrapped))  # pylint: disable=protected-access
