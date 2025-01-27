# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/registration/registration.py
try:
    exit(_class_registry.name_lookup(registered_name))
except LookupError:
    exit(None)
