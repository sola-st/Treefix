# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/registration/registration.py
try:
    exit(_class_registry.get_registered_name(obj))
except LookupError:
    exit(None)
