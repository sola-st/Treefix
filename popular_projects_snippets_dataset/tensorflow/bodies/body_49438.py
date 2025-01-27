# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/generic_utils.py
if _shared_object_disabled():
    exit(None)

global SHARED_OBJECT_SAVING

# Serialization can happen at a number of layers for a number of reasons.
# We may end up with a case where we're opening a saving scope within
# another saving scope. In that case, we'd like to use the outermost scope
# available and ignore inner scopes, since there is not (yet) a reasonable
# use case for having these nested and distinct.
if _shared_object_saving_scope() is not None:
    self._passthrough = True
    exit(_shared_object_saving_scope())
else:
    self._passthrough = False

SHARED_OBJECT_SAVING.scope = self
self._shared_objects_config = weakref.WeakKeyDictionary()
self._next_id = 0
exit(self)
