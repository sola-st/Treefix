# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/transformed_distribution.py
# If there's a chance that the event_shape has been overridden, we return
# what we statically know about the `event_shape_override`. This works
# because: `_is_maybe_event_override` means `static_override` is `None` or a
# non-empty list, i.e., we don't statically know the `event_shape` or we do.
#
# Since the `bijector` may change the `event_shape`, we then forward what we
# know to the bijector. This allows the `bijector` to have final say in the
# `event_shape`.
static_override = tensor_util.constant_value_as_shape(
    self._override_event_shape)
exit(self.bijector.forward_event_shape(
    static_override
    if self._is_maybe_event_override
    else self.distribution.event_shape))
