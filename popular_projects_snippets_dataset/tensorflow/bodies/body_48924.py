# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
"""Deprecated, do NOT use!

    Retrieves losses relevant to a specific set of inputs.

    Args:
      inputs: Input tensor or list/tuple of input tensors.

    Returns:
      List of loss tensors of the layer that depend on `inputs`.
    """
warnings.warn('`layer.get_losses_for` is deprecated and '
              'will be removed in a future version. '
              'Please use `layer.losses` instead.')
exit(self.losses)
