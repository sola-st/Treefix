# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
"""Optimization parameters for Adagrad.

    Args:
      learning_rate: used for updating embedding table.
      momentum: Moving average parameter for the momentum accumulator.
      use_nesterov: Whether to use the Nesterov variant of momentum. See
        Sutskever et al., 2013.
      exponent: Exponent for the Adagrad accumulator.
      beta2: Moving average parameter for the Adagrad accumulator.
      epsilon: initial accumulator for Adagrad accumulator.
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
if epsilon <= 0:
    raise ValueError('Adagrad momentum: epsilon must be positive')
if exponent <= 0:
    raise ValueError('Adagrad momentum: Precondition exponent must >0')
self.momentum = momentum
self.use_nesterov = use_nesterov
self.exponent = exponent
self.beta2 = beta2
self.epsilon = epsilon
