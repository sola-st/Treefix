# Extracted from ./data/repos/tensorflow/tensorflow/python/training/ftrl.py
self._learning_rate_tensor = ops.convert_to_tensor(
    self._learning_rate, name="learning_rate")
self._l1_regularization_strength_tensor = ops.convert_to_tensor(
    self._l1_regularization_strength, name="l1_regularization_strength")
# L2 regularization strength with beta added in so that the underlying
# TensorFlow ops do not need to include that parameter.
self._adjusted_l2_regularization_strength_tensor = ops.convert_to_tensor(
    self._l2_regularization_strength + self._beta /
    (2. * math_ops.maximum(self._learning_rate, 1e-36)),
    name="adjusted_l2_regularization_strength")
assert self._adjusted_l2_regularization_strength_tensor is not None
self._beta_tensor = ops.convert_to_tensor(self._beta, name="beta")
self._l2_shrinkage_regularization_strength_tensor = ops.convert_to_tensor(
    self._l2_shrinkage_regularization_strength,
    name="l2_shrinkage_regularization_strength")
self._learning_rate_power_tensor = ops.convert_to_tensor(
    self._learning_rate_power, name="learning_rate_power")
