# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/device_util.py
"""Partially canonicalize device string.

  This returns device string from `d` without including job and task.
  This is most useful for parameter server strategy where the device strings are
  generated on the chief, but executed on workers.

   For example:
    If d = '/cpu:0', default='/job:worker/task:1', it returns
      '/replica:0/device:CPU:0'.
    If d = '/cpu:0', default='/job:worker', it returns
      '/replica:0/device:CPU:0'.
    If d = '/gpu:0', default=None, it returns
      '/replica:0/device:GPU:0'.

  Note: This uses "job:localhost" as the default if executing eagerly.

  Args:
    d: a device string or tf.config.LogicalDevice

  Returns:
    a partially canonicalized device string.
  """
canonicalized_device = canonicalize(d)
spec = tf_device.DeviceSpec.from_string(canonicalized_device)
spec = spec.replace(job=None, task=None, replica=0)
exit(spec.to_string())
