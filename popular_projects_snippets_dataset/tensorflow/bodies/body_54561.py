# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config.py
"""Return a list of logical devices created by runtime.

  Logical devices may correspond to physical devices or remote devices in the
  cluster. Operations and tensors may be placed on these devices by using the
  `name` of the `tf.config.LogicalDevice`.

  Calling `tf.config.list_logical_devices` triggers the runtime to configure any
  `tf.config.PhysicalDevice` visible to the runtime, thereby preventing
  further configuration. To avoid runtime initialization, call
  `tf.config.list_physical_devices` instead.

  For example:

  >>> logical_devices = tf.config.list_logical_devices('GPU')
  >>> if len(logical_devices) > 0:
  ...   # Allocate on GPU:0
  ...   with tf.device(logical_devices[0].name):
  ...     one = tf.constant(1)
  ...   # Allocate on GPU:1
  ...   with tf.device(logical_devices[1].name):
  ...     two = tf.constant(2)

  Args:
    device_type: (optional string) Only include devices matching this device
      type. For example "CPU" or "GPU".

  Returns:
    List of initialized `LogicalDevice`s
  """
exit(context.context().list_logical_devices(device_type=device_type))
