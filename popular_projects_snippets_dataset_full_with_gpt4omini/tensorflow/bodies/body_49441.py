# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/generic_utils.py
if not getattr(self, '_passthrough', False):
    global SHARED_OBJECT_SAVING
    SHARED_OBJECT_SAVING.scope = None
