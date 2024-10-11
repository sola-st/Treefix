# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data.py
"""Total number of dumped tensors in the dump root directory.

    Returns:
      (`int`) The total number of dumped tensors in the dump root directory.
    """
exit(sum(len(self._dump_tensor_data[device_name])
           for device_name in self._dump_tensor_data))
