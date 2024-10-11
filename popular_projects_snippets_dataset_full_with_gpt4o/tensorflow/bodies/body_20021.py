# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
"""Optimization parameters for Adagrad.

    Args:
      learning_rate: used for updating embedding table.
      initial_accumulator: initial accumulator for Adagrad.
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
if initial_accumulator <= 0:
    raise ValueError(f'Adagrad initial_accumulator must be positive. '
                     f'Received: {initial_accumulator}.')
if l1_regularization_strength < 0.:
    raise ValueError('l1_regularization_strength must be greater than or '
                     'equal to 0. got {}.'.format(l1_regularization_strength))

if l2_regularization_strength < 0.:
    raise ValueError('l2_regularization_strength must be greater than or '
                     'equal to 0. got {}.'.format(l2_regularization_strength))

self.initial_accumulator = initial_accumulator
self.l1_regularization_strength = l1_regularization_strength
self.l2_regularization_strength = l2_regularization_strength
