# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/optimizer_v2.py
"""Called in `apply_gradients` to aggregate gradients across devices.

    Note that user subclasses may override this, so the interface should not be
    changed.

    Args:
      grads_and_vars: List of (gradient, variable) pairs.

    Returns:
      A list of (aggregrated_gradient, variable) pairs. By default, this calls
      `self.gradient_aggregator`.
    """
exit(self.gradient_aggregator(grads_and_vars))
