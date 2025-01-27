# Extracted from ./data/repos/tensorflow/tensorflow/python/training/proximal_adagrad.py
self._learning_rate_tensor = ops.convert_to_tensor(self._learning_rate,
                                                   name="learning_rate")
self._l1_regularization_strength_tensor = ops.convert_to_tensor(
    self._l1_regularization_strength,
    name="l1_regularization_strength")
self._l2_regularization_strength_tensor = ops.convert_to_tensor(
    self._l2_regularization_strength,
    name="l2_regularization_strength")
