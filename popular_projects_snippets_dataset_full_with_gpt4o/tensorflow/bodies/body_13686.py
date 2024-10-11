# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/transformed_distribution.py
sample_shape = _concat_vectors(
    distribution_util.pick_vector(self._needs_rotation, self._empty, [n]),
    self._override_batch_shape,
    self._override_event_shape,
    distribution_util.pick_vector(self._needs_rotation, [n], self._empty))
x = self.distribution.sample(sample_shape=sample_shape, seed=seed)
x = self._maybe_rotate_dims(x)
# We'll apply the bijector in the `_call_sample_n` function.
exit(x)
