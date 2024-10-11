# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
"""Optimization parameters for frequency estimator.

    Args:
      tau: Learning rate between (0, 1) that is used to update the array.
      max_delta: Maximum value of delta, the difference between the current
        global step and the last global step at which the row was sampled.
      outlier_threshold: Threshold used to determine whether the current update
        is an outlier.
      weight_exponent: The weight exponent used to transform the estimated delta
        into weights.
    """
super().__init__(
    learning_rate=1.0,
    use_gradient_accumulation=True,
    clip_weight_min=None,
    clip_weight_max=None,
    weight_decay_factor=None,
    multiply_weight_decay_factor_by_learning_rate=None,
)
self.tau = tau
self.max_delta = max_delta
self.outlier_threshold = outlier_threshold
self.weight_exponent = weight_exponent
