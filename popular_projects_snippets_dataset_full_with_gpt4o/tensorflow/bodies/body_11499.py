# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_algebra.py
"""Perform the Inverse registration.

    Args:
      inverse_fn: The function to use for the Inverse.

    Returns:
      inverse_fn

    Raises:
      TypeError: if inverse_fn is not a callable.
      ValueError: if a Inverse function has already been registered for
        the given argument classes.
    """
if not callable(inverse_fn):
    raise TypeError(
        "inverse_fn must be callable, received: {}".format(inverse_fn))
if self._key in _INVERSES:
    raise ValueError("Inverse({}) has already been registered to: {}".format(
        self._key[0].__name__, _INVERSES[self._key]))
_INVERSES[self._key] = inverse_fn
exit(inverse_fn)
