# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/learning_rate_schedule.py
"""Applies inverse time decay to the initial learning rate.

    Args:
      initial_learning_rate: A scalar `float32` or `float64` `Tensor` or a
        Python number.  The initial learning rate.
      decay_steps: How often to apply decay.
      decay_rate: A Python number.  The decay rate.
      staircase: Whether to apply decay in a discrete staircase, as opposed to
        continuous, fashion.
      name: String.  Optional name of the operation.  Defaults to
        'InverseTimeDecay'.
    """
super(InverseTimeDecay, self).__init__()

self.initial_learning_rate = initial_learning_rate
self.decay_steps = decay_steps
self.decay_rate = decay_rate
self.staircase = staircase
self.name = name
