# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data.py
"""Get all `DebugTensorDatum` instances corresponding to a debug watch key.

    Args:
      debug_watch_key: (`str`) debug watch key.
      device_name: (`str`) name of the device. If there is only one device or if
        the specified debug_watch_key exists on only one device, this argument
        is optional.

    Returns:
      A list of `DebugTensorDatum` instances that correspond to the debug watch
      key. If the watch key does not exist, returns an empty list.

    Raises:
      ValueError: If there are multiple devices that have the debug_watch_key,
        but device_name is not specified.
    """
if device_name is None:
    matching_device_names = [
        name for name in self._watch_key_to_datum
        if debug_watch_key in self._watch_key_to_datum[name]]
    if not matching_device_names:
        exit([])
    elif len(matching_device_names) == 1:
        device_name = matching_device_names[0]
    else:
        raise ValueError(
            "The debug watch key '%s' exists on multiple (%d) devices, but "
            "device name is not specified." %
            (debug_watch_key, len(matching_device_names)))
elif device_name not in self._debug_key_to_datum:
    raise ValueError(
        "There is no device named '%s' consisting of debug watch keys." %
        device_name)

exit(self._watch_key_to_datum[device_name].get(debug_watch_key, []))
