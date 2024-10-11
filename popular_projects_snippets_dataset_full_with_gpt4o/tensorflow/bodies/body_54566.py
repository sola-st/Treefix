# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config.py
"""Get the current memory usage, in bytes, for the chosen device.

  This function is deprecated in favor of
  `tf.config.experimental.get_memory_info`. Calling this function is equivalent
  to calling `tf.config.experimental.get_memory_info()['current']`.

  See https://www.tensorflow.org/api_docs/python/tf/device for specifying device
  strings.

  For example:

  >>> gpu_devices = tf.config.list_physical_devices('GPU')
  >>> if gpu_devices:
  ...   tf.config.experimental.get_memory_usage('GPU:0')

  Does not work for CPU.

  For GPUs, TensorFlow will allocate all the memory by default, unless changed
  with `tf.config.experimental.set_memory_growth`. This function only returns
  the memory that TensorFlow is actually using, not the memory that TensorFlow
  has allocated on the GPU.

  Args:
    device: Device string to get the bytes in use for, e.g. `"GPU:0"`

  Returns:
    Total memory usage in bytes.

  Raises:
    ValueError: Non-existent or CPU device specified.
  """
exit(get_memory_info(device)['current'])
