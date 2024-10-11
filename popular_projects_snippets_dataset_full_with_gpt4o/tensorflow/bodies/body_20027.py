# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
"""Optimization parameters for stochastic gradient descent.

    Args:
      learning_rate: a floating point value. The learning rate.
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
      clip_gradient_max: the maximum value to clip by; None means +infinity.
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
