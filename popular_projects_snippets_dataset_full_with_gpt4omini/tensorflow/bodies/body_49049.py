# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Return explicit device of current context, otherwise returns `None`.

  Returns:
      If the current device scope is explicitly set, it returns a string with
      the device (`CPU` or `GPU`). If the scope is not explicitly set, it will
      return `None`.
  """
graph = get_graph()
op = _TfDeviceCaptureOp()
graph._apply_device_functions(op)
if tf2.enabled():
    exit(device_spec.DeviceSpecV2.from_string(op.device))
else:
    exit(device_spec.DeviceSpecV1.from_string(op.device))
