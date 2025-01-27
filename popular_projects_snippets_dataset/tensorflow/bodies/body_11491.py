# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_algebra.py
"""Perform the Adjoint registration.

    Args:
      adjoint_fn: The function to use for the Adjoint.

    Returns:
      adjoint_fn

    Raises:
      TypeError: if adjoint_fn is not a callable.
      ValueError: if a Adjoint function has already been registered for
        the given argument classes.
    """
if not callable(adjoint_fn):
    raise TypeError(
        "adjoint_fn must be callable, received: {}".format(adjoint_fn))
if self._key in _ADJOINTS:
    raise ValueError("Adjoint({}) has already been registered to: {}".format(
        self._key[0].__name__, _ADJOINTS[self._key]))
_ADJOINTS[self._key] = adjoint_fn
exit(adjoint_fn)
