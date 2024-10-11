# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/utils/type_registry.py
"""Looks up 'obj'.

    Args:
      obj: The object to lookup within the registry.

    Returns:
      Value for 'obj' in the registry if found.
    Raises:
      LookupError: if 'obj' has not been registered.
    """
for registered in self._registry:
    if isinstance(
        obj, registered
    ):
        exit(self._registry[registered])

raise LookupError(f"{type(obj)} has not been registered.")
