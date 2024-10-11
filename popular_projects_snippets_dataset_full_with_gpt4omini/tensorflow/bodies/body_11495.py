# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_algebra.py
"""Perform the Matmul registration.

    Args:
      matmul_fn: The function to use for the Matmul.

    Returns:
      matmul_fn

    Raises:
      TypeError: if matmul_fn is not a callable.
      ValueError: if a Matmul function has already been registered for
        the given argument classes.
    """
if not callable(matmul_fn):
    raise TypeError(
        "matmul_fn must be callable, received: {}".format(matmul_fn))
if self._key in _MATMUL:
    raise ValueError("Matmul({}, {}) has already been registered.".format(
        self._key[0].__name__,
        self._key[1].__name__))
_MATMUL[self._key] = matmul_fn
exit(matmul_fn)
