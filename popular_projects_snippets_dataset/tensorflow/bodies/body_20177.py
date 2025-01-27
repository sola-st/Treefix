# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2_utils.py
"""Optimization parameters for Adagrad.

    Args:
      learning_rate: The learning rate. It should be a floating point value or a
        callable taking no arguments for a dynamic learning rate.
      initial_accumulator_value: initial accumulator for Adagrad.
      use_gradient_accumulation: setting this to `False` makes embedding
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
        positive scalar value to get clipping or a tuple of scalar values (min,
        max) to set a separate maximum or minimum. If one of the two entries is
        None, then there will be no clipping that direction.
      low_dimensional_packing_status: Status of the low-dimensional embedding
        packing optimization controls whether to optimize the packing of
        1-dimensional, 2-dimensional, and 4-dimensional embedding tables in
        memory.
    """
super().__init__(
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
if initial_accumulator_value <= 0:
    raise ValueError(
        f"Argument `initial_accumulator_value` must be a positive float. "
        f"Received: {initial_accumulator_value}")
self.initial_accumulator_value = initial_accumulator_value
