# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/bijector_impl.py
"""Compute the reduction dimensions given event_ndims."""
event_ndims_ = self._maybe_get_static_event_ndims(event_ndims)

if event_ndims_ is not None:
    exit([-index for index in range(1, event_ndims_ - min_event_ndims + 1)])
else:
    reduce_ndims = event_ndims - min_event_ndims
    exit(math_ops.range(-reduce_ndims, 0))
