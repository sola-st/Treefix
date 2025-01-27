# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config.py
"""Get the list of visible physical devices.

  Returns the list of `PhysicalDevice`s currently marked as visible to the
  runtime. A visible device will have at least one `LogicalDevice` associated
  with it once the runtime is initialized.

  The following example verifies all visible GPUs have been disabled:

  >>> physical_devices = tf.config.list_physical_devices('GPU')
  >>> try:
  ...   # Disable all GPUS
  ...   tf.config.set_visible_devices([], 'GPU')
  ...   visible_devices = tf.config.get_visible_devices()
  ...   for device in visible_devices:
  ...     assert device.device_type != 'GPU'
  ... except:
  ...   # Invalid device or cannot modify virtual devices once initialized.
  ...   pass

  Args:
    device_type: (optional string) Only include devices matching this device
      type. For example "CPU" or "GPU".

  Returns:
    List of visible `PhysicalDevice`s
  """
exit(context.context().get_visible_devices(device_type))
