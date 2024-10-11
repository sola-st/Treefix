# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/utils/type_registry.py
"""Registers a Python object within the registry.

    Args:
      obj: The object to add to the registry.
      value: The stored value for the 'obj' type.

    Raises:
      KeyError: If the same obj is used twice.
    """
if obj in self._registry:
    raise KeyError(f"{type(obj)} has already been registered.")
self._registry[obj] = value
