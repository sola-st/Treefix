# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/dtensor_device.py
"""Returns the number of cache hit and miss for function compilation.

    Returns:
      A dictionary keyed with miss and hit, corresponding to the cache hit and
      miss count.
    """
exit(_pywrap_dtensor_device.GetFunctionCacheHitAndMissCount(
    context.context()._handle,  # pylint: disable=protected-access,
    self._device_info))
