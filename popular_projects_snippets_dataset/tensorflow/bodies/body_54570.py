# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config.py
"""Get the virtual device configuration for a `tf.config.PhysicalDevice`.

  Returns the list of `tf.config.LogicalDeviceConfiguration`
  objects previously configured by a call to
  `tf.config.set_logical_device_configuration`.

  For example:

  >>> physical_devices = tf.config.list_physical_devices('CPU')
  >>> assert len(physical_devices) == 1, "No CPUs found"
  >>> configs = tf.config.get_logical_device_configuration(
  ...   physical_devices[0])
  >>> try:
  ...   assert configs is None
  ...   tf.config.set_logical_device_configuration(
  ...     physical_devices[0],
  ...     [tf.config.LogicalDeviceConfiguration(),
  ...      tf.config.LogicalDeviceConfiguration()])
  ...   configs = tf.config.get_logical_device_configuration(
  ...     physical_devices[0])
  ...   assert len(configs) == 2
  ... except:
  ...   # Cannot modify virtual devices once initialized.
  ...   pass

  Args:
    device: `PhysicalDevice` to query

  Returns:
    List of `tf.config.LogicalDeviceConfiguration` objects or
    `None` if no virtual device configuration has been set for this physical
    device.
  """
exit(context.context().get_logical_device_configuration(device))
