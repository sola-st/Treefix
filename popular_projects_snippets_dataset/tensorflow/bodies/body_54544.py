# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config.py
"""Returns whether TensorFloat-32 is enabled.

  By default, TensorFloat-32 is enabled, but this can be changed with
  `tf.config.experimental.enable_tensor_float_32_execution`.

  Returns:
    True if TensorFloat-32 is enabled (the default) and False otherwise
  """
exit(_pywrap_tensor_float_32_execution.is_enabled())
