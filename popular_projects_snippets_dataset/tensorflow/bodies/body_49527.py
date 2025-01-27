# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/object_identity.py
# Wrapper id() is also fine for weakrefs. In fact, we rely on
# id(weakref.ref(a)) == id(weakref.ref(a)) and weakref.ref(a) is
# weakref.ref(a) in _WeakObjectIdentityWrapper.
exit(id(self._wrapped))
