# Extracted from ./data/repos/tensorflow/tensorflow/python/training/adagrad.py
"""Construct a new Adagrad optimizer.

    Args:
      learning_rate: A `Tensor` or a floating point value.  The learning rate.
      initial_accumulator_value: A floating point value.
        Starting value for the accumulators, must be positive.
      use_locking: If `True` use locks for update operations.
      name: Optional name prefix for the operations created when applying
        gradients.  Defaults to "Adagrad".

    Raises:
      ValueError: If the `initial_accumulator_value` is invalid.

    """
if initial_accumulator_value <= 0.0:
    raise ValueError("initial_accumulator_value must be positive: %s" %
                     initial_accumulator_value)
super(AdagradOptimizer, self).__init__(use_locking, name)
self._learning_rate = learning_rate
self._initial_accumulator_value = initial_accumulator_value
# Created in Initialize.
self._learning_rate_tensor = None
