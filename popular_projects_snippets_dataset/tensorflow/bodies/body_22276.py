# Extracted from ./data/repos/tensorflow/tensorflow/python/training/adagrad_da.py
"""Construct a new AdagradDA optimizer.

    Args:
      learning_rate: A `Tensor` or a floating point value.  The learning rate.
      global_step: A `Tensor` containing the current training step number.
      initial_gradient_squared_accumulator_value: A floating point value.
        Starting value for the accumulators, must be positive.
      l1_regularization_strength: A float value, must be greater than or
        equal to zero.
      l2_regularization_strength: A float value, must be greater than or
        equal to zero.
      use_locking: If `True` use locks for update operations.
      name: Optional name prefix for the operations created when applying
        gradients.  Defaults to "AdagradDA".

    Raises:
      ValueError: If the `initial_gradient_squared_accumulator_value` is
      invalid.
    """
if initial_gradient_squared_accumulator_value <= 0.0:
    raise ValueError("initial_gradient_squared_accumulator_value must be "
                     "positive: %s" %
                     initial_gradient_squared_accumulator_value)
super(AdagradDAOptimizer, self).__init__(use_locking, name)
self._learning_rate = learning_rate
self._initial_gradient_squared_accumulator_value = (
    initial_gradient_squared_accumulator_value)
# Created in Initialize.
self._learning_rate_tensor = None
self._l1_regularization_strength = l1_regularization_strength
self._l2_regularization_strength = l2_regularization_strength
self._global_step = global_step
self._global_step_on_worker = None
