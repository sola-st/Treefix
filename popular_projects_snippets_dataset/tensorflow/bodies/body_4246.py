# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/dtensor_device.py
"""Guess layouts using the layouts of other tensors with the same shape.

    This is the default behavior, and is quite safe. The `default_layout` scope
    overrides shape-based guesses.

    Args:
      enabled: A boolean indicating whether to use the policy.
    """
_pywrap_dtensor_device.SetSameShapePolicy(self._device_info, enabled)
