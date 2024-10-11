# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/transformed_distribution.py
# If there's a chance that the batch_shape has been overridden, we return
# what we statically know about the `batch_shape_override`. This works
# because: `_is_maybe_batch_override` means `static_override` is `None` or a
# non-empty list, i.e., we don't statically know the `batch_shape` or we do.
#
# Notice that this implementation parallels the `_event_shape` except that
# the `bijector` doesn't get to alter the `batch_shape`. Recall that
# `batch_shape` is a property of a distribution while `event_shape` is
# shared between both the `distribution` instance and the `bijector`.
static_override = tensor_util.constant_value_as_shape(
    self._override_batch_shape)
exit((static_override
        if self._is_maybe_batch_override
        else self.distribution.batch_shape))
