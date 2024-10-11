# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
"""Optimization parameters for Ftrl.

    Implements FTRL as described in the following [paper](
    https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/41159.pdf)

    Args:
      learning_rate: a floating point value. The learning rate.
      learning_rate_power: A float value, must be less or equal to zero.
        Controls how the learning rate decreases during training. Use zero for a
        fixed learning rate. See section 3.1 in the
        [paper](https://www.eecs.tufts.edu/~dsculley/papers/ad-click-prediction.pdf).
      initial_accumulator_value: The starting value for accumulators. Only zero
        or positive values are allowed.
      l1_regularization_strength: A float value, must be greater than or equal
        to zero.
      l2_regularization_strength: A float value, must be greater than or equal
        to zero.
      use_gradient_accumulation: setting this to `False` makes embedding
        gradients calculation less accurate but faster. Please see
        `optimization_parameters.proto` for details. for details.
      clip_weight_min: the minimum value to clip by; None means -infinity.
      clip_weight_max: the maximum value to clip by; None means +infinity.
      weight_decay_factor: amount of weight decay to apply; None means that the
        weights are not decayed.
      multiply_weight_decay_factor_by_learning_rate: if true,
        `weight_decay_factor` is multiplied by the current learning rate.
      multiply_linear_by_learning_rate: When true, multiplies the usages of the
        linear slot in the weight update by the learning rate. This is useful
        when ramping up learning rate from 0 (which would normally produce
        NaNs).
      beta: The beta parameter for FTRL.
      allow_zero_accumulator: Changes the implementation of the square root to
        allow for the case of initial_accumulator_value being zero. This will
        cause a slight performance drop.
      clip_gradient_min: the minimum value to clip by; None means -infinity.
        Gradient accumulation must be set to true if this is set.
      clip_gradient_max: the maximum value to clip by; None means +infinity.
        Gradient accumulation must be set to true if this is set.
    """
super().__init__(
    learning_rate=learning_rate,
    use_gradient_accumulation=use_gradient_accumulation,
    clip_weight_min=clip_weight_min,
    clip_weight_max=clip_weight_max,
    weight_decay_factor=weight_decay_factor,
    multiply_weight_decay_factor_by_learning_rate=(
        multiply_weight_decay_factor_by_learning_rate),
    clip_gradient_min=clip_gradient_min,
    clip_gradient_max=clip_gradient_max,
)
if learning_rate_power > 0.:
    raise ValueError('learning_rate_power must be less than or equal to 0. '
                     'got {}.'.format(learning_rate_power))

if initial_accumulator_value < 0.:
    raise ValueError('initial_accumulator_value must be greater than or equal'
                     ' to 0. got {}.'.format(initial_accumulator_value))

if l1_regularization_strength < 0.:
    raise ValueError('l1_regularization_strength must be greater than or '
                     'equal to 0. got {}.'.format(l1_regularization_strength))

if l2_regularization_strength < 0.:
    raise ValueError('l2_regularization_strength must be greater than or '
                     'equal to 0. got {}.'.format(l2_regularization_strength))

self.learning_rate_power = learning_rate_power
self.initial_accumulator_value = initial_accumulator_value
self.initial_linear_value = 0.0
self.l1_regularization_strength = l1_regularization_strength
self.l2_regularization_strength = l2_regularization_strength
self.multiply_linear_by_learning_rate = multiply_linear_by_learning_rate
self.beta = beta
self.allow_zero_accumulator = allow_zero_accumulator
