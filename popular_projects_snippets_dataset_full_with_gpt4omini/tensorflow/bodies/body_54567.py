# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config.py
"""Get if memory growth is enabled for a `PhysicalDevice`.

  If memory growth is enabled for a `PhysicalDevice`, the runtime initialization
  will not allocate all memory on the device.

  For example:

  >>> physical_devices = tf.config.list_physical_devices('GPU')
  >>> try:
  ...   tf.config.experimental.set_memory_growth(physical_devices[0], True)
  ...   assert tf.config.experimental.get_memory_growth(physical_devices[0])
  ... except:
  ...   # Invalid device or cannot modify virtual devices once initialized.
  ...   pass

  Args:
    device: `PhysicalDevice` to query

  Returns:
    A boolean indicating the memory growth setting for the `PhysicalDevice`.

  Raises:
    ValueError: Invalid `PhysicalDevice` specified.
  """
exit(context.context().get_memory_growth(device))
