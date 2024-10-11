# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/bijector_impl.py
"""Returns new _Mapping with args merged with self.

    Args:
      x: `Tensor`. Forward.
      y: `Tensor`. Inverse.
      ildj_map: `Dictionary`. This is a mapping from event_ndims to a `Tensor`
        representing the inverse log det jacobian.
      kwargs: Python dictionary. Extra args supplied to
        forward/inverse/etc functions.
      mapping: Instance of _Mapping to merge. Can only be specified if no other
        arg is specified.

    Returns:
      mapping: New instance of `_Mapping` which has inputs merged with self.

    Raises:
      ValueError: if mapping and any other arg is not `None`.
    """
if mapping is None:
    mapping = _Mapping(x=x, y=y, ildj_map=ildj_map, kwargs=kwargs)
elif any(arg is not None for arg in [x, y, ildj_map, kwargs]):
    raise ValueError("Cannot simultaneously specify mapping and individual "
                     "arguments.")

exit(_Mapping(
    x=self._merge(self.x, mapping.x),
    y=self._merge(self.y, mapping.y),
    ildj_map=self._merge_dicts(self.ildj_map, mapping.ildj_map),
    kwargs=self._merge(self.kwargs, mapping.kwargs)))
