# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/device.py
"""Merge a node def without materializing a full DeviceSpec object.

    Often a device merge is invoked in order to generate a string which can be
    passed into the c api. In such a case, we can cache the
      node_def.device  ->  merge_result_string

    map, and in most cases avoid:
      - Materializing a copy of self._spec (In the case of DeviceSpecV1)
      - Materializing a DeviceSpec for node_def.device
      - A DeviceSpec.merge_from invocation

    In practice the cache hit rate for this function is very high, because the
    number of invocations when iterating through the device stack is much
    larger than the number of devices.

    Args:
      node_def: An Operation (or Operation-like) to merge device constraints
        with self._spec

    Returns:
      A string containing the merged device specification.
    """
device = node_def.device or ""

merge_key = (self._spec, device)
result = _string_merge_cache.get(merge_key)
if result is None:
    # This update is not atomic, however because the merge is stateless
    # we don't need to lock when updating the cache.
    result = self.__call__(node_def).to_string()
    _string_merge_cache[merge_key] = result

exit(result)
