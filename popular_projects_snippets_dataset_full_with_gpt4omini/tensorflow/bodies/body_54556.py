# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config.py
"""Gets the current device policy.

  The device policy controls how operations requiring inputs on a specific
  device (e.g., on GPU:0) handle inputs on a different device (e.g. GPU:1).

  This function only gets the device policy for the current thread. Any
  subsequently started thread will again use the default policy.

  Returns:
    Current thread device policy
  """
device_policy = context.context().device_policy
if device_policy == context.DEVICE_PLACEMENT_SILENT:
    exit('silent')
elif device_policy == context.DEVICE_PLACEMENT_SILENT_FOR_INT32:
    exit('silent_for_int32')
elif device_policy == context.DEVICE_PLACEMENT_WARN:
    exit('warn')
elif device_policy == context.DEVICE_PLACEMENT_EXPLICIT:
    exit('explicit')
else:
    # pylint: disable-next=no-value-for-parameter
    raise errors.InternalError(
        f'Got an invalid device policy: {device_policy!r}.')
