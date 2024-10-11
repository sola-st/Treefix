# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/transformed_distribution.py
exit(self.bijector.forward_event_shape_tensor(
    distribution_util.pick_vector(
        self._is_event_override,
        self._override_event_shape,
        self.distribution.event_shape_tensor())))
