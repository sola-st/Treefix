# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config.py
"""Resets the tracked memory stats for the chosen device.

  This function sets the tracked peak memory for a device to the device's
  current memory usage. This allows you to measure the peak memory usage for a
  specific part of your program. For example:

  >>> if tf.config.list_physical_devices('GPU'):
  ...   # Sets the peak memory to the current memory.
  ...   tf.config.experimental.reset_memory_stats('GPU:0')
  ...   # Creates the first peak memory usage.
  ...   x1 = tf.ones(1000 * 1000, dtype=tf.float64)
  ...   del x1 # Frees the memory referenced by `x1`.
  ...   peak1 = tf.config.experimental.get_memory_info('GPU:0')['peak']
  ...   # Sets the peak memory to the current memory again.
  ...   tf.config.experimental.reset_memory_stats('GPU:0')
  ...   # Creates the second peak memory usage.
  ...   x2 = tf.ones(1000 * 1000, dtype=tf.float32)
  ...   del x2
  ...   peak2 = tf.config.experimental.get_memory_info('GPU:0')['peak']
  ...   assert peak2 < peak1  # tf.float32 consumes less memory than tf.float64.

  Currently only supports GPU and TPU. If called on a CPU device, an exception
  will be raised.

  Args:
    device: Device string to reset the memory stats, e.g. `"GPU:0"`, `"TPU:0"`.
      See https://www.tensorflow.org/api_docs/python/tf/device for specifying
      device strings.

  Raises:
    ValueError: No device found with the device name, like '"nonexistent"'.
    ValueError: Invalid device name, like '"GPU"', '"CPU:GPU"', '"CPU:"'.
    ValueError: Multiple devices matched with the device name.
    ValueError: Memory statistics not tracked or clearing memory statistics not
      supported, like '"CPU:0"'.
  """
context.context().reset_memory_stats(device)
