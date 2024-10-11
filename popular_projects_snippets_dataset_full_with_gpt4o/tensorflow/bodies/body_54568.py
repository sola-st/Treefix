# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config.py
"""Set if memory growth should be enabled for a `PhysicalDevice`.

  If memory growth is enabled for a `PhysicalDevice`, the runtime initialization
  will not allocate all memory on the device. Memory growth cannot be configured
  on a `PhysicalDevice` with virtual devices configured.

  For example:

  >>> physical_devices = tf.config.list_physical_devices('GPU')
  >>> try:
  ...   tf.config.experimental.set_memory_growth(physical_devices[0], True)
  ... except:
  ...   # Invalid device or cannot modify virtual devices once initialized.
  ...   pass

  Args:
    device: `PhysicalDevice` to configure
    enable: (Boolean) Whether to enable or disable memory growth

  Raises:
    ValueError: Invalid `PhysicalDevice` specified.
    RuntimeError: Runtime is already initialized.
  """
context.context().set_memory_growth(device, enable)
