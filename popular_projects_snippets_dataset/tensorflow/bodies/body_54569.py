# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config.py
"""Returns details about a physical devices.

  This API takes in a `tf.config.PhysicalDevice` returned by
  `tf.config.list_physical_devices`. It returns a dict with string keys
  containing various details about the device. Each key is only supported by a
  subset of devices, so you should not assume the returned dict will have any
  particular key.

  >>> gpu_devices = tf.config.list_physical_devices('GPU')
  >>> if gpu_devices:
  ...   details = tf.config.experimental.get_device_details(gpu_devices[0])
  ...   details.get('device_name', 'Unknown GPU')

  Currently, details are only returned for GPUs. This function returns an
  empty dict if passed a non-GPU device.

  The returned dict may have the following keys:
  * `'device_name'`: A human-readable name of the device as a string, e.g.
    "Titan V". Unlike `tf.config.PhysicalDevice.name`, this will be the same for
    multiple devices if each device is the same model. Currently only available
    for GPUs.
  * `'compute_capability'`: The
    [compute capability](https://developer.nvidia.com/cuda-gpus) of the device
    as a tuple of two ints, in the form `(major_version, minor_version)`. Only
    available for NVIDIA GPUs

  Note: This is similar to `tf.sysconfig.get_build_info` in that both functions
  can return information relating to GPUs. However, this function returns
  run-time information about a specific device (such as a GPU's compute
  capability), while `tf.sysconfig.get_build_info` returns compile-time
  information about how TensorFlow was built (such as what version of CUDA
  TensorFlow was built for).

  Args:
    device: A `tf.config.PhysicalDevice` returned by
      `tf.config.list_physical_devices` or `tf.config.get_visible_devices`.

  Returns:
    A dict with string keys.
  """
exit(context.context().get_device_details(device))
