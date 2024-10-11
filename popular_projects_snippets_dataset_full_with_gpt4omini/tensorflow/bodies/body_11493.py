# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_algebra.py
"""Perform the Cholesky registration.

    Args:
      cholesky_fn: The function to use for the Cholesky.

    Returns:
      cholesky_fn

    Raises:
      TypeError: if cholesky_fn is not a callable.
      ValueError: if a Cholesky function has already been registered for
        the given argument classes.
    """
if not callable(cholesky_fn):
    raise TypeError(
        "cholesky_fn must be callable, received: {}".format(cholesky_fn))
if self._key in _CHOLESKY_DECOMPS:
    raise ValueError("Cholesky({}) has already been registered to: {}".format(
        self._key[0].__name__, _CHOLESKY_DECOMPS[self._key]))
_CHOLESKY_DECOMPS[self._key] = cholesky_fn
exit(cholesky_fn)
