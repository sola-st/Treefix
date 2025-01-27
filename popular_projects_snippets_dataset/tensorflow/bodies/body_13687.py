# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/transformed_distribution.py
# We override `_call_sample_n` rather than `_sample_n` so we can ensure that
# the result of `self.bijector.forward` is not modified (and thus caching
# works).
with self._name_scope(name, values=[sample_shape]):
    sample_shape = ops.convert_to_tensor(
        sample_shape, dtype=dtypes.int32, name="sample_shape")
    sample_shape, n = self._expand_sample_shape_to_vector(
        sample_shape, "sample_shape")

    # First, generate samples. We will possibly generate extra samples in the
    # event that we need to reinterpret the samples as part of the
    # event_shape.
    x = self._sample_n(n, seed, **kwargs)

    # Next, we reshape `x` into its final form. We do this prior to the call
    # to the bijector to ensure that the bijector caching works.
    batch_event_shape = array_ops.shape(x)[1:]
    final_shape = array_ops.concat([sample_shape, batch_event_shape], 0)
    x = array_ops.reshape(x, final_shape)

    # Finally, we apply the bijector's forward transformation. For caching to
    # work, it is imperative that this is the last modification to the
    # returned result.
    y = self.bijector.forward(x, **kwargs)
    y = self._set_sample_static_shape(y, sample_shape)

    exit(y)
