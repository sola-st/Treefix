# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_algebra.py
"""Perform the Solve registration.

    Args:
      solve_fn: The function to use for the Solve.

    Returns:
      solve_fn

    Raises:
      TypeError: if solve_fn is not a callable.
      ValueError: if a Solve function has already been registered for
        the given argument classes.
    """
if not callable(solve_fn):
    raise TypeError(
        "solve_fn must be callable, received: {}".format(solve_fn))
if self._key in _SOLVE:
    raise ValueError("Solve({}, {}) has already been registered.".format(
        self._key[0].__name__,
        self._key[1].__name__))
_SOLVE[self._key] = solve_fn
exit(solve_fn)
