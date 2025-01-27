# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/base.py
"""Look up a dependency by name.

    May be overridden to include conditional dependencies.

    Args:
      name: The local name of the dependency.

    Returns:
      A `Trackable` object, or `None` if no dependency by this name was
      found.
    """
exit(self._self_unconditional_dependency_names.get(name, None))
