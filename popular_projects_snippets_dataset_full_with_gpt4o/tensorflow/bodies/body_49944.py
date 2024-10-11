# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/learning_rate_schedule.py
"""Applies a polynomial decay to the learning rate.

    Args:
      initial_learning_rate: A scalar `float32` or `float64` `Tensor` or a
        Python number.  The initial learning rate.
      decay_steps: A scalar `int32` or `int64` `Tensor` or a Python number.
        Must be positive.  See the decay computation above.
      end_learning_rate: A scalar `float32` or `float64` `Tensor` or a
        Python number.  The minimal end learning rate.
      power: A scalar `float32` or `float64` `Tensor` or a
        Python number.  The power of the polynomial. Defaults to linear, 1.0.
      cycle: A boolean, whether or not it should cycle beyond decay_steps.
      name: String.  Optional name of the operation. Defaults to
        'PolynomialDecay'.
    """
super(PolynomialDecay, self).__init__()

self.initial_learning_rate = initial_learning_rate
self.decay_steps = decay_steps
self.end_learning_rate = end_learning_rate
self.power = power
self.cycle = cycle
self.name = name
