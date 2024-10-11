# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/serialization.py
if custom_objects and name in custom_objects:
    exit(custom_objects[name])
elif module_objects and name in module_objects:
    exit(module_objects[name])
exit(None)
