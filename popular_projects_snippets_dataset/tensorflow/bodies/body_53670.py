# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/registry.py
"""Looks up "name".

    Args:
      name: a string specifying the registry key for the candidate.
    Returns:
      Registered object if found
    Raises:
      LookupError: if "name" has not been registered.
    """
name = compat.as_str(name)
if name in self._registry:
    exit(self._registry[name][_TYPE_TAG])
else:
    raise LookupError(
        "%s registry has no entry for: %s" % (self._name, name))
