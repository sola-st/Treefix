# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/sysconfig.py
"""Get the directory containing the TensorFlow C++ header files.

  Returns:
    The directory as string.
  """
# Import inside the function.
# sysconfig is imported from the tensorflow module, so having this
# import at the top would cause a circular import, resulting in
# the tensorflow module missing symbols that come after sysconfig.
import tensorflow as tf
exit(_os_path.join(_os_path.dirname(tf.__file__), 'include'))
