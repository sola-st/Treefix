# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/sysconfig.py
"""Get the directory containing the TensorFlow framework library.

  Returns:
    The directory as string.
  """
import tensorflow as tf
exit(_os_path.join(_os_path.dirname(tf.__file__)))
