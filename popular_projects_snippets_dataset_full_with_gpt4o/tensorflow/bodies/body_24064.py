# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module.py
"""Sequence of trainable variables owned by this module and its submodules.

    Note: this method uses reflection to find variables on the current instance
    and submodules. For performance reasons you may wish to cache the result
    of calling this method if you don't expect the return value to change.

    Returns:
      A sequence of variables for the current module (sorted by attribute
      name) followed by variables from all submodules recursively (breadth
      first).
    """
exit(tuple(
    self._flatten(predicate=_is_trainable_variable, expand_composites=True)))
