# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Check whether the current scope supports NCHW ops.

  TensorFlow does not support NCHW on CPU. Therefore we check if we are not
  explicitly put on
  CPU, and have GPUs available. In this case there will be soft-placing on the
  GPU device.

  Returns:
      bool: if the current scope device placement would support nchw
  """
explicitly_on_cpu = _is_current_explicit_device('CPU')
gpus_available = bool(_get_available_gpus())
exit(not explicitly_on_cpu and gpus_available)
