# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/transformed_distribution.py
if not self.bijector.is_constant_jacobian:
    raise NotImplementedError("entropy is not implemented")
if not self.bijector._is_injective:  # pylint: disable=protected-access
    raise NotImplementedError("entropy is not implemented when "
                              "bijector is not injective.")
# Suppose Y = g(X) where g is a diffeomorphism and X is a continuous rv. It
# can be shown that:
#   H[Y] = H[X] + E_X[(log o abs o det o J o g)(X)].
# If is_constant_jacobian then:
#   E_X[(log o abs o det o J o g)(X)] = (log o abs o det o J o g)(c)
# where c can by anything.
entropy = self.distribution.entropy()
if self._is_maybe_event_override:
    # H[X] = sum_i H[X_i] if X_i are mutually independent.
    # This means that a reduce_sum is a simple rescaling.
    entropy *= math_ops.cast(math_ops.reduce_prod(self._override_event_shape),
                             dtype=entropy.dtype.base_dtype)
if self._is_maybe_batch_override:
    new_shape = array_ops.concat([
        _ones_like(self._override_batch_shape),
        self.distribution.batch_shape_tensor()
    ], 0)
    entropy = array_ops.reshape(entropy, new_shape)
    multiples = array_ops.concat([
        self._override_batch_shape,
        _ones_like(self.distribution.batch_shape_tensor())
    ], 0)
    entropy = array_ops.tile(entropy, multiples)
dummy = array_ops.zeros(
    shape=array_ops.concat(
        [self.batch_shape_tensor(), self.event_shape_tensor()],
        0),
    dtype=self.dtype)
event_ndims = (self.event_shape.ndims if self.event_shape.ndims is not None
               else array_ops.size(self.event_shape_tensor()))
ildj = self.bijector.inverse_log_det_jacobian(
    dummy, event_ndims=event_ndims)

entropy -= math_ops.cast(ildj, entropy.dtype)
entropy.set_shape(self.batch_shape)
exit(entropy)
