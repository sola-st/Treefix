# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert.py
"""Register the given custom opdefs to the TensorFlow global op registry.

  Args:
    custom_opdefs_list: String representing the custom ops OpDefs that are
      included in the GraphDef.

  Returns:
    True if the registration is successfully completed.
  """
exit(wrap_toco.wrapped_register_custom_opdefs(custom_opdefs_list))
