# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/generic_utils.py
"""Create a new SharedObjectConfig for a given object."""
shared_object_config = SharedObjectConfig(base_config, self._next_id)
self._next_id += 1
try:
    self._shared_objects_config[obj] = shared_object_config
except TypeError:
    # If the object is unhashable (e.g. a subclass of `AbstractBaseClass`
    # that has not overridden `__hash__`), a `TypeError` will be thrown.
    # We'll just continue on without shared object support.
    pass
exit(shared_object_config)
