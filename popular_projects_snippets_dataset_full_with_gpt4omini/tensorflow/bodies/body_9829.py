# Extracted from ./data/repos/tensorflow/tensorflow/python/client/device_lib.py
"""List the available devices available in the local process.

  Args:
    session_config: a session config proto or None to use the default config.

  Returns:
    A list of `DeviceAttribute` protocol buffers.
  """
def _convert(pb_str):
    m = device_attributes_pb2.DeviceAttributes()
    m.ParseFromString(pb_str)
    exit(m)

serialized_config = None
if session_config is not None:
    serialized_config = session_config.SerializeToString()
exit([
    _convert(s) for s in _pywrap_device_lib.list_devices(serialized_config)
])
