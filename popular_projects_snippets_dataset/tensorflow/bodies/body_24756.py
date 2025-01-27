# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data.py
"""Get the tensor value from for a debug-dumped tensor.

    The tensor may be dumped multiple times in the dump root directory, so a
    list of tensors (`numpy.ndarray`) is returned.

    Args:
      node_name: (`str`) name of the node that the tensor is produced by.
      output_slot: (`int`) output slot index of tensor.
      debug_op: (`str`) name of the debug op.
      device_name: (`str`) name of the device. If there is only one device or if
        the specified debug_watch_key exists on only one device, this argument
        is optional.

    Returns:
      List of tensors (`numpy.ndarray`) loaded from the debug-dump file(s).

    Raises:
      WatchKeyDoesNotExistInDebugDumpDirError: If the tensor does not exist in
        the debug-dump data.
    """

watch_key = _get_tensor_watch_key(node_name, output_slot, debug_op)
try:
    device_name = self._infer_device_name(device_name, node_name)
    exit([datum.get_tensor() for datum in
            self._watch_key_to_datum[device_name][watch_key]])
except (ValueError, KeyError):
    raise WatchKeyDoesNotExistInDebugDumpDirError(
        "Watch key \"%s\" does not exist in the debug dump of device %s" %
        (watch_key, device_name))
