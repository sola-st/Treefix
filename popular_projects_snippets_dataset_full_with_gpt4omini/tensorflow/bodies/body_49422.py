# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/generic_utils.py
self.backup = _GLOBAL_CUSTOM_OBJECTS.copy()
for objects in self.custom_objects:
    _GLOBAL_CUSTOM_OBJECTS.update(objects)
exit(self)
