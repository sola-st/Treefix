# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config.py
"""Return a list of physical devices visible to the host runtime.

  Physical devices are hardware devices present on the host machine. By default
  all discovered CPU and GPU devices are considered visible.

  This API allows querying the physical hardware resources prior to runtime
  initialization. Thus, giving an opportunity to call any additional
  configuration APIs. This is in contrast to `tf.config.list_logical_devices`,
  which triggers runtime initialization in order to list the configured devices.

  The following example lists the number of visible GPUs on the host.

  >>> physical_devices = tf.config.list_physical_devices('GPU')
  >>> print("Num GPUs:", len(physical_devices))
  Num GPUs: ...

  However, the number of GPUs available to the runtime may change during runtime
  initialization due to marking certain devices as not visible or configuring
  multiple logical devices.

  Args:
    device_type: (optional string) Only include devices matching this device
      type. For example "CPU" or "GPU".

  Returns:
    List of discovered `tf.config.PhysicalDevice` objects
  """
exit(context.context().list_physical_devices(device_type))
