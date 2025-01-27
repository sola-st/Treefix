# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2_utils.py
"""Optimization parameters for Adam.

    See 'tensorflow/core/protobuf/tpu/optimization_parameters.proto' for a
    complete description of these parameters and their impacts on the optimizer
    algorithm.

    Args:
      learning_rate: The learning rate. It should be a floating point value or a
        callable taking no arguments for a dynamic learning rate.
      beta_1: A float value. The exponential decay rate for the 1st moment
        estimates.
      beta_2: A float value. The exponential decay rate for the 2nd moment
        estimates.
      epsilon: A small constant for numerical stability.
      lazy_adam: Use lazy Adam instead of Adam. Lazy Adam trains faster.
      sum_inside_sqrt: When this is true, the Adam update formula is changed
        from `m / (sqrt(v) + epsilon)` to `m / sqrt(v + epsilon**2)`. This
        option improves the performance of TPU training and is not expected to
        harm model quality.
      use_gradient_accumulation: Setting this to `False` makes embedding
        gradients calculation less accurate but faster.
      clip_weight_min: the minimum value to clip by; None means -infinity.
      clip_weight_max: the maximum value to clip by; None means +infinity.
      weight_decay_factor: amount of weight decay to apply; None means that the
        weights are not decayed.
      multiply_weight_decay_factor_by_learning_rate: if true,
        `weight_decay_factor` is multiplied by the current learning rate.
      slot_variable_creation_fn: If you wish do directly control the creation of
        the slot variables, set this to a callable taking three parameters: a
        table variable, a list of slot names to create for it, and a list of
        initializers. This function should return a dict with the slot names as
        keys and the created variables as values with types matching the table
        variable. When set to None (the default), uses the built-in variable
        creation.
      clipvalue: Controls clipping of the gradient. Set to either a single
        positive scalar value to get clipping or a tiple of scalar values (min,
        max) to set a separate maximum or minimum. If one of the two entries is
        None, then there will be no clipping that direction.
      low_dimensional_packing_status: Status of the low-dimensional embedding
        packing optimization controls whether to optimize the packing of
        1-dimensional, 2-dimensional, and 4-dimensional embedding tables in
        memory.
    """
super(Adam, self).__init__(
    learning_rate,
    use_gradient_accumulation,
    clip_weight_min,
    clip_weight_max,
    weight_decay_factor,
    multiply_weight_decay_factor_by_learning_rate,
    clipvalue,
    slot_variable_creation_fn,
    low_dimensional_packing_status,
)
if beta_1 < 0. or beta_1 >= 1.:
    raise ValueError(
        f"Argument `beta_1` must be >= 0 and < 1. Received: {beta_1}.")
if beta_2 < 0. or beta_2 >= 1.:
    raise ValueError(
        f"Argument `beta_2` must be >= 0 and < 1. Received: {beta_1}.")
if epsilon <= 0.:
    raise ValueError("epsilon must be positive; got {}.".format(epsilon))
if not use_gradient_accumulation and not lazy_adam:
    raise ValueError(
        "When disabling lazy Adam (`lazy_adam=False`), "
        "gradient accumulation must be used. "
        "Set `use_gradient_accumulation` to False.")

self.beta_1 = beta_1
self.beta_2 = beta_2
self.epsilon = epsilon
self.lazy_adam = lazy_adam
self.sum_inside_sqrt = sum_inside_sqrt
