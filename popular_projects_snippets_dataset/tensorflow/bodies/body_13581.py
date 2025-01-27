# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/kullback_leibler.py
"""Perform the KL registration.

    Args:
      kl_fn: The function to use for the KL divergence.

    Returns:
      kl_fn

    Raises:
      TypeError: if kl_fn is not a callable.
      ValueError: if a KL divergence function has already been registered for
        the given argument classes.
    """
if not callable(kl_fn):
    raise TypeError("kl_fn must be callable, received: %s" % kl_fn)
if self._key in _DIVERGENCES:
    raise ValueError("KL(%s || %s) has already been registered to: %s"
                     % (self._key[0].__name__, self._key[1].__name__,
                        _DIVERGENCES[self._key]))
_DIVERGENCES[self._key] = kl_fn
exit(kl_fn)
