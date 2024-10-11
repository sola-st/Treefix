# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/device_util.py
"""Canonicalize device string.

  If d has missing components, the rest would be deduced from the `default`
  argument or from '/replica:0/task:0/device:CPU:0'. For example:
    If d = '/cpu:0', default='/job:worker/task:1', it returns
      '/job:worker/replica:0/task:1/device:CPU:0'.
    If d = '/cpu:0', default='/job:worker', it returns
      '/job:worker/replica:0/task:0/device:CPU:0'.
    If d = '/gpu:0', default=None, it returns
      '/replica:0/task:0/device:GPU:0'.

  Note: This uses "job:localhost" as the default if executing eagerly.

  Args:
    d: a device string or tf.config.LogicalDevice
    default: a string for default device if d doesn't have all components.

  Returns:
    a canonicalized device string.
  """
if isinstance(d, context.LogicalDevice):
    d = tf_device.DeviceSpec.from_string(d.name)
else:
    d = tf_device.DeviceSpec.from_string(d)

assert d.device_type is None or d.device_type == d.device_type.upper(), (
    "Device type '%s' must be all-caps." % (d.device_type,))
# Fill in missing device fields using defaults.
result = tf_device.DeviceSpec(
    replica=0, task=0, device_type="CPU", device_index=0)
if ops.executing_eagerly_outside_functions():
    # Try to deduce job, replica and task in case it's in a multi worker setup.
    # TODO(b/151452748): Using list_logical_devices is not always safe since it
    # may return remote devices as well, but we're already doing this elsewhere.
    host_cpu = tf_device.DeviceSpec.from_string(
        config.list_logical_devices("CPU")[0].name)
    if host_cpu.job:
        result = result.make_merged_spec(host_cpu)
    else:
        # The default job is localhost if eager execution is enabled
        result = result.replace(job="localhost")
if default:
    # Overrides any defaults with values from the default device if given.
    result = result.make_merged_spec(
        tf_device.DeviceSpec.from_string(default))

# Apply `d` last, so that it's values take precedence over the defaults.
result = result.make_merged_spec(d)
exit(result.to_string())
