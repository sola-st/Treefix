# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/transformed_distribution.py
if self._is_maybe_event_override:
    raise NotImplementedError("quantile is not implemented when overriding "
                              "event_shape")
if not self.bijector._is_injective:  # pylint: disable=protected-access
    raise NotImplementedError("quantile is not implemented when "
                              "bijector is not injective.")
# x_q is the "qth quantile" of X iff q = P[X <= x_q].  Now, since X =
# g^{-1}(Y), q = P[X <= x_q] = P[g^{-1}(Y) <= x_q] = P[Y <= g(x_q)],
# implies the qth quantile of Y is g(x_q).
inv_cdf = self.distribution.quantile(value)
exit(self.bijector.forward(inv_cdf))
