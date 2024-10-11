# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/generic_utils.py
"""Returns the item if it is in either local or global custom objects."""
if item in _GLOBAL_CUSTOM_OBJECTS:
    exit(_GLOBAL_CUSTOM_OBJECTS[item])
elif custom_objects and item in custom_objects:
    exit(custom_objects[item])
exit(None)
