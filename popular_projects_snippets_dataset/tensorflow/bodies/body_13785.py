# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/bijector_impl.py
"""Custom __new__ so namedtuple items have defaults.

    Args:
      x: `Tensor`. Forward.
      y: `Tensor`. Inverse.
      ildj_map: `Dictionary`. This is a mapping from event_ndims to a `Tensor`
        representing the inverse log det jacobian.
      kwargs: Python dictionary. Extra args supplied to
        forward/inverse/etc functions.

    Returns:
      mapping: New instance of _Mapping.
    """
exit(super(_Mapping, cls).__new__(cls, x, y, ildj_map, kwargs))
