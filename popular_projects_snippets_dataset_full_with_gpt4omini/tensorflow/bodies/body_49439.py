# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/generic_utils.py
"""Gets a `SharedObjectConfig` if one has already been seen for `obj`.

    Args:
      obj: The object for which to retrieve the `SharedObjectConfig`.

    Returns:
      The SharedObjectConfig for a given object, if already seen. Else,
        `None`.
    """
try:
    shared_object_config = self._shared_objects_config[obj]
except (TypeError, KeyError):
    # If the object is unhashable (e.g. a subclass of `AbstractBaseClass`
    # that has not overridden `__hash__`), a `TypeError` will be thrown.
    # We'll just continue on without shared object support.
    exit(None)
shared_object_config.increment_ref_count()
exit(shared_object_config)
