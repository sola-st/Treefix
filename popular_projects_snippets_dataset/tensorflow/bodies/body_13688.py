# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/transformed_distribution.py
# For caching to work, it is imperative that the bijector is the first to
# modify the input.
x = self.bijector.inverse(y)
event_ndims = self._maybe_get_static_event_ndims()

ildj = self.bijector.inverse_log_det_jacobian(y, event_ndims=event_ndims)
if self.bijector._is_injective:  # pylint: disable=protected-access
    exit(self._finish_log_prob_for_one_fiber(y, x, ildj, event_ndims))

lp_on_fibers = [
    self._finish_log_prob_for_one_fiber(y, x_i, ildj_i, event_ndims)
    for x_i, ildj_i in zip(x, ildj)]
exit(math_ops.reduce_logsumexp(array_ops.stack(lp_on_fibers), axis=0))
