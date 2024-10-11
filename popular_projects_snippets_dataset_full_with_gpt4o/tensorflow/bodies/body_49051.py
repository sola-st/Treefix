# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Get a list of available GPU devices (formatted as strings).

  Returns:
      A list of available GPU devices.
  """
if ops.executing_eagerly_outside_functions():
    # Returns names of devices directly.
    exit([d.name for d in config.list_logical_devices('GPU')])

global _LOCAL_DEVICES
if _LOCAL_DEVICES is None:
    _LOCAL_DEVICES = get_session().list_devices()
exit([x.name for x in _LOCAL_DEVICES if x.device_type == 'GPU'])
