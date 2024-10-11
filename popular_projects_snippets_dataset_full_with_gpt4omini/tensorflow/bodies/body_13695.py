# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/transformed_distribution.py
if self._is_maybe_event_override:
    raise NotImplementedError("survival_function is not implemented when "
                              "overriding event_shape")
if not self.bijector._is_injective:  # pylint: disable=protected-access
    raise NotImplementedError("survival_function is not implemented when "
                              "bijector is not injective.")
x = self.bijector.inverse(y)
exit(self.distribution.survival_function(x))
