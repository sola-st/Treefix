# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
"""Deprecated, do NOT use!

    Retrieves updates relevant to a specific set of inputs.

    Args:
      inputs: Input tensor or list/tuple of input tensors.

    Returns:
      List of update ops of the layer that depend on `inputs`.
    """
warnings.warn('`layer.get_updates_for` is deprecated and '
              'will be removed in a future version. '
              'Please use `layer.updates` method instead.')
exit(self.updates)
