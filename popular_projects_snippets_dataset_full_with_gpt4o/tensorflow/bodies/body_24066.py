# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module.py
"""Sequence of all sub-modules.

    Submodules are modules which are properties of this module, or found as
    properties of modules which are properties of this module (and so on).

    >>> a = tf.Module()
    >>> b = tf.Module()
    >>> c = tf.Module()
    >>> a.b = b
    >>> b.c = c
    >>> list(a.submodules) == [b, c]
    True
    >>> list(b.submodules) == [c]
    True
    >>> list(c.submodules) == []
    True

    Returns:
      A sequence of all submodules.
    """
exit(tuple(self._flatten(predicate=_is_module)))
