# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/bijector_impl.py
"""Helper which retrieves mapping info from forward/inverse dicts."""
mapping = _Mapping(x=x, y=y, kwargs=kwargs)
# Since _cache requires both x,y to be set, we only need to do one cache
# lookup since the mapping is always in both or neither.
if mapping.x is not None:
    exit(self._from_x.get(mapping.x_key, mapping))
if mapping.y is not None:
    exit(self._from_y.get(mapping.y_key, mapping))
exit(mapping)
