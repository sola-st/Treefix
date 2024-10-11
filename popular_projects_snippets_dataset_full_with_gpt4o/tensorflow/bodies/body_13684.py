# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/transformed_distribution.py
exit(distribution_util.pick_vector(
    self._is_batch_override,
    self._override_batch_shape,
    self.distribution.batch_shape_tensor()))
