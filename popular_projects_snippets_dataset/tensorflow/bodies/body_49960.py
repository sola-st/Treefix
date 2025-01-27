# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/learning_rate_schedule.py
"""Applies noisy linear cosine decay to the learning rate.

    Args:
      initial_learning_rate: A scalar `float32` or `float64` Tensor or a Python
        number. The initial learning rate.
      decay_steps: A scalar `int32` or `int64` `Tensor` or a Python number.
        Number of steps to decay over.
      initial_variance: initial variance for the noise. See computation above.
      variance_decay: decay for the noise's variance. See computation above.
      num_periods: Number of periods in the cosine part of the decay.
        See computation above.
      alpha: See computation above.
      beta: See computation above.
      name: String.  Optional name of the operation.  Defaults to
        'NoisyLinearCosineDecay'.
    """
super(NoisyLinearCosineDecay, self).__init__()

self.initial_learning_rate = initial_learning_rate
self.decay_steps = decay_steps
self.initial_variance = initial_variance
self.variance_decay = variance_decay
self.num_periods = num_periods
self.alpha = alpha
self.beta = beta
self.name = name
