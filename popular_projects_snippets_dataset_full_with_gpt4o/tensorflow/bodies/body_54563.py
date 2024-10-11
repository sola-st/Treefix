# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config.py
"""Set the list of visible devices.

  Specifies which `PhysicalDevice` objects are visible to the runtime.
  TensorFlow will only allocate memory and place operations on visible
  physical devices, as otherwise no `LogicalDevice` will be created on them.
  By default all discovered devices are marked as visible.

  The following example demonstrates disabling the first GPU on the machine.

  >>> physical_devices = tf.config.list_physical_devices('GPU')
  >>> try:
  ...   # Disable first GPU
  ...   tf.config.set_visible_devices(physical_devices[1:], 'GPU')
  ...   logical_devices = tf.config.list_logical_devices('GPU')
  ...   # Logical device was not created for first GPU
  ...   assert len(logical_devices) == len(physical_devices) - 1
  ... except:
  ...   # Invalid device or cannot modify virtual devices once initialized.
  ...   pass

  Args:
    devices: List of `PhysicalDevice`s to make visible
    device_type: (optional) Only configure devices matching this device type.
      For example "CPU" or "GPU". Other devices will be left unaltered.

  Raises:
    ValueError: If argument validation fails.
    RuntimeError: Runtime is already initialized.
  """
context.context().set_visible_devices(devices, device_type)
