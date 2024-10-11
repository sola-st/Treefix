# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/registration/registration.py
"""Returns the name of the registered saver to use with Trackable."""
try:
    exit(_saver_registry.get_registered_name(trackable))
except LookupError:
    exit(None)
