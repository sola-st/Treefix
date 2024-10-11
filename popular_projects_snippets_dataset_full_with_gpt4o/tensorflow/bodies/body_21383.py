# Extracted from ./data/repos/tensorflow/tensorflow/python/training/proximal_adagrad.py
"""Construct a new ProximalAdagrad optimizer.

    Args:
      learning_rate: A `Tensor` or a floating point value.  The learning rate.
      initial_accumulator_value: A floating point value.
        Starting value for the accumulators, must be positive.
      l1_regularization_strength: A float value, must be greater than or
        equal to zero.
      l2_regularization_strength: A float value, must be greater than or
        equal to zero.
      use_locking: If `True` use locks for update operations.
      name: Optional name prefix for the operations created when applying
        gradients.  Defaults to "Adagrad".

    Raises:
      ValueError: If the `initial_accumulator_value` is invalid.
    """
if initial_accumulator_value <= 0.0:
    raise ValueError("initial_accumulator_value must be positive: %s" %
                     initial_accumulator_value)
super(ProximalAdagradOptimizer, self).__init__(use_locking, name)
self._learning_rate = learning_rate
self._initial_accumulator_value = initial_accumulator_value
self._l1_regularization_strength = l1_regularization_strength
self._l2_regularization_strength = l2_regularization_strength
# Created in Initialize.
self._l1_regularization_strength_tensor = None
self._l2_regularization_strength_tensor = None
self._learning_rate_tensor = None
