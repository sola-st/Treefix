# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/dtensor_device.py
"""Translates TPU core locations to TPU core IDs.

    Args:
      tpu_core_locations: A list of TPU core locations. Each one is a list of
        four unsigned integers, [x, y, z, core].

    Returns:
      A list of corresponding TPU core IDs.
    """
exit(_pywrap_dtensor_device.TPUCoreLocationsToIDs(
    context.context()._handle,  # pylint: disable=protected-access
    self._device_info,
    tpu_core_locations))
