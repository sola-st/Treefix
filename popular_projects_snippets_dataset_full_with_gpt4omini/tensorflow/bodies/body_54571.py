# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config.py
"""Set the logical device configuration for a `tf.config.PhysicalDevice`.

  A visible `tf.config.PhysicalDevice` will by default have a single
  `tf.config.LogicalDevice` associated with it once the runtime is initialized.
  Specifying a list of `tf.config.LogicalDeviceConfiguration` objects allows
  multiple devices to be created on the same `tf.config.PhysicalDevice`.

  Logical device configurations can be modified by calling this function as
  long as the runtime is uninitialized. After the runtime is initialized
  calling this function raises a RuntimeError.

  The following example splits the CPU into 2 logical devices:

  >>> physical_devices = tf.config.list_physical_devices('CPU')
  >>> assert len(physical_devices) == 1, "No CPUs found"
  >>> # Specify 2 virtual CPUs. Note currently memory limit is not supported.
  >>> try:
  ...   tf.config.set_logical_device_configuration(
  ...     physical_devices[0],
  ...     [tf.config.LogicalDeviceConfiguration(),
  ...      tf.config.LogicalDeviceConfiguration()])
  ...   logical_devices = tf.config.list_logical_devices('CPU')
  ...   assert len(logical_devices) == 2
  ...
  ...   tf.config.set_logical_device_configuration(
  ...     physical_devices[0],
  ...     [tf.config.LogicalDeviceConfiguration(),
  ...      tf.config.LogicalDeviceConfiguration(),
  ...      tf.config.LogicalDeviceConfiguration(),
  ...      tf.config.LogicalDeviceConfiguration()])
  ... except:
  ...   # Cannot modify logical devices once initialized.
  ...   pass

  The following example splits the GPU into 2 logical devices with 100 MB each:

  >>> physical_devices = tf.config.list_physical_devices('GPU')
  >>> try:
  ...   tf.config.set_logical_device_configuration(
  ...     physical_devices[0],
  ...     [tf.config.LogicalDeviceConfiguration(memory_limit=100),
  ...      tf.config.LogicalDeviceConfiguration(memory_limit=100)])
  ...
  ...   logical_devices = tf.config.list_logical_devices('GPU')
  ...   assert len(logical_devices) == len(physical_devices) + 1
  ...
  ...   tf.config.set_logical_device_configuration(
  ...     physical_devices[0],
  ...     [tf.config.LogicalDeviceConfiguration(memory_limit=10),
  ...      tf.config.LogicalDeviceConfiguration(memory_limit=10)])
  ... except:
  ...   # Invalid device or cannot modify logical devices once initialized.
  ...   pass

  Args:
    device: The `PhysicalDevice` to configure.
    logical_devices: (optional) List of `tf.config.LogicalDeviceConfiguration`
      objects to allocate for the specified `PhysicalDevice`. If None, the
      default configuration will be used.

  Raises:
    ValueError: If argument validation fails.
    RuntimeError: Runtime is already initialized.
  """
context.context().set_logical_device_configuration(device, logical_devices)
