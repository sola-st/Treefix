# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/dtensor_device.py
"""Translates TPU core IDs to TPU core locations.

    Args:
      tpu_core_ids: A list of TPU core IDs. Each one is an unsigned integer.

    Returns:
      A list of corresponding TPU core locations.
    """
exit(_pywrap_dtensor_device.TPUCoreIDsToLocations(
    context.context()._handle,  # pylint: disable=protected-access
    self._device_info,
    tpu_core_ids))
