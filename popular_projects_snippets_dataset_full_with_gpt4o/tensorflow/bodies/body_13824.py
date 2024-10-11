# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/bijector_impl.py
"""Helper which stores mapping info in forward/inverse dicts."""
# Merging from lookup is an added check that we're not overwriting anything
# which is not None.
mapping = mapping.merge(mapping=self._lookup(
    mapping.x, mapping.y, mapping.kwargs))
if mapping.x is None and mapping.y is None:
    raise ValueError("Caching expects at least one of (x,y) to be known, "
                     "i.e., not None.")
self._from_x[mapping.x_key] = mapping
self._from_y[mapping.y_key] = mapping
