# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/bijector_impl.py
"""Reduce jacobian over event_ndims - min_event_ndims."""
# In this case, we need to tile the Jacobian over the event and reduce.
y_rank = array_ops.rank(y)
y_shape = array_ops.shape(y)[
    y_rank - event_ndims : y_rank - min_event_ndims]

ones = array_ops.ones(y_shape, ildj.dtype)
reduced_ildj = math_ops.reduce_sum(
    ones * ildj,
    axis=self._get_event_reduce_dims(min_event_ndims, event_ndims))
# The multiplication by ones can change the inferred static shape so we try
# to recover as much as possible.
event_ndims_ = self._maybe_get_static_event_ndims(event_ndims)
if (event_ndims_ is not None and
    y.shape.ndims is not None and
    ildj.shape.ndims is not None):
    y_shape = y.shape[y.shape.ndims - event_ndims_ :
                      y.shape.ndims - min_event_ndims]
    broadcast_shape = array_ops.broadcast_static_shape(ildj.shape, y_shape)
    reduced_ildj.set_shape(
        broadcast_shape[: broadcast_shape.ndims - (
            event_ndims_ - min_event_ndims)])

exit(reduced_ildj)
