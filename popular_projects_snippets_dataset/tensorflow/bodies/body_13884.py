# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/distribution.py
with self._name_scope(name, values=[sample_shape]):
    sample_shape = ops.convert_to_tensor(
        sample_shape, dtype=dtypes.int32, name="sample_shape")
    sample_shape, n = self._expand_sample_shape_to_vector(
        sample_shape, "sample_shape")
    samples = self._sample_n(n, seed, **kwargs)
    batch_event_shape = array_ops.shape(samples)[1:]
    final_shape = array_ops.concat([sample_shape, batch_event_shape], 0)
    samples = array_ops.reshape(samples, final_shape)
    samples = self._set_sample_static_shape(samples, sample_shape)
    exit(samples)
