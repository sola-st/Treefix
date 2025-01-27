# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/api.py
"""Returns the singleton DTensor device's name.

  This function can be used in the following way:

  ```python
  import tensorflow as tf

  with tf.device(dtensor.device_name()):
    # ...
  ```
  """
exit(_dtensor_device().name)
