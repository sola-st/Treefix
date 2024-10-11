# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/transformed_distribution.py
"""Finish computation of log_prob on one element of the inverse image."""
x = self._maybe_rotate_dims(x, rotate_right=True)
log_prob = self.distribution.log_prob(x)
if self._is_maybe_event_override:
    log_prob = math_ops.reduce_sum(log_prob, self._reduce_event_indices)
log_prob += math_ops.cast(ildj, log_prob.dtype)
if self._is_maybe_event_override and isinstance(event_ndims, int):
    log_prob.set_shape(
        array_ops.broadcast_static_shape(
            y.get_shape().with_rank_at_least(1)[:-event_ndims],
            self.batch_shape))
exit(log_prob)
