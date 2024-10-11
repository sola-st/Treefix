# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/generic_utils.py
if _shared_object_disabled():
    exit(NoopLoadingScope())

global SHARED_OBJECT_LOADING
SHARED_OBJECT_LOADING.scope = self
self._obj_ids_to_obj = {}
exit(self)
