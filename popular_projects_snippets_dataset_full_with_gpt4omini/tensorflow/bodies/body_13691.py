# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/transformed_distribution.py
"""Finish computation of prob on one element of the inverse image."""
x = self._maybe_rotate_dims(x, rotate_right=True)
prob = self.distribution.prob(x)
if self._is_maybe_event_override:
    prob = math_ops.reduce_prod(prob, self._reduce_event_indices)
prob *= math_ops.exp(math_ops.cast(ildj, prob.dtype))
if self._is_maybe_event_override and isinstance(event_ndims, int):
    prob.set_shape(
        array_ops.broadcast_static_shape(
            y.get_shape().with_rank_at_least(1)[:-event_ndims],
            self.batch_shape))
exit(prob)
