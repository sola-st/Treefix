# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/learning_rate_schedule.py
"""Applies exponential decay to the learning rate.

    Args:
      initial_learning_rate: A scalar `float32` or `float64` `Tensor` or a
        Python number.  The initial learning rate.
      decay_steps: A scalar `int32` or `int64` `Tensor` or a Python number.
        Must be positive.  See the decay computation above.
      decay_rate: A scalar `float32` or `float64` `Tensor` or a
        Python number.  The decay rate.
      staircase: Boolean.  If `True` decay the learning rate at discrete
        intervals
      name: String.  Optional name of the operation.  Defaults to
        'ExponentialDecay'.
    """
super(ExponentialDecay, self).__init__()
self.initial_learning_rate = initial_learning_rate
self.decay_steps = decay_steps
self.decay_rate = decay_rate
self.staircase = staircase
self.name = name
