# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config.py
"""Get memory info for the chosen device, as a dict.

  This function returns a dict containing information about the device's memory
  usage. For example:

  >>> if tf.config.list_physical_devices('GPU'):
  ...   # Returns a dict in the form {'current': <current mem usage>,
  ...   #                             'peak': <peak mem usage>}
  ...   tf.config.experimental.get_memory_info('GPU:0')

  Currently returns the following keys:
    - `'current'`: The current memory used by the device, in bytes.
    - `'peak'`: The peak memory used by the device across the run of the
        program, in bytes. Can be reset with
        `tf.config.experimental.reset_memory_stats`.

  More keys may be added in the future, including device-specific keys.

  Currently only supports GPU and TPU. If called on a CPU device, an exception
  will be raised.

  For GPUs, TensorFlow will allocate all the memory by default, unless changed
  with `tf.config.experimental.set_memory_growth`. The dict specifies only the
  current and peak memory that TensorFlow is actually using, not the memory that
  TensorFlow has allocated on the GPU.

  Args:
    device: Device string to get the memory information for, e.g. `"GPU:0"`,
    `"TPU:0"`. See https://www.tensorflow.org/api_docs/python/tf/device for
      specifying device strings.

  Returns:
    A dict with keys `'current'` and `'peak'`, specifying the current and peak
    memory usage respectively.

  Raises:
    ValueError: No device found with the device name, like '"nonexistent"'.
    ValueError: Invalid device name, like '"GPU"', '"CPU:GPU"', '"CPU:"'.
    ValueError: Multiple devices matched with the device name.
    ValueError: Memory statistics not tracked, like '"CPU:0"'.
  """
exit(context.context().get_memory_info(device))
