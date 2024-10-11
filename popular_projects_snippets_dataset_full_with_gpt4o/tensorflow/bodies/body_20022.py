# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
"""Optimization parameters for Adam.

    Args:
      learning_rate: a floating point value. The learning rate.
      beta1: A float value. The exponential decay rate for the 1st moment
        estimates.
      beta2: A float value. The exponential decay rate for the 2nd moment
        estimates.
      epsilon: A small constant for numerical stability.
      lazy_adam: Use lazy Adam instead of Adam. Lazy Adam trains faster. See
        `optimization_parameters.proto` for details.
      sum_inside_sqrt: This improves training speed. Please see
        `optimization_parameters.proto` for details.
      use_gradient_accumulation: setting this to `False` makes embedding
        gradients calculation less accurate but faster. Please see
        `optimization_parameters.proto` for details.
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
if beta1 < 0. or beta1 >= 1.:
    raise ValueError('beta1 must be between 0. and 1; got {}.'.format(beta1))
if beta2 < 0. or beta2 >= 1.:
    raise ValueError('beta2 must be between 0. and 1; got {}.'.format(beta2))
if epsilon <= 0.:
    raise ValueError('epsilon must be positive; got {}.'.format(epsilon))
if not use_gradient_accumulation and not lazy_adam:
    raise ValueError(
        'When disabling Lazy Adam, gradient accumulation must be used.')

self.beta1 = beta1
self.beta2 = beta2
self.epsilon = epsilon
self.lazy_adam = lazy_adam
self.sum_inside_sqrt = sum_inside_sqrt
