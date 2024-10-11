# Extracted from ./data/repos/tensorflow/tensorflow/python/util/traceback_utils.py
"""Check whether traceback filtering is currently enabled.

  See also `tf.debugging.enable_traceback_filtering()` and
  `tf.debugging.disable_traceback_filtering()`. Note that filtering out
  internal frames from the tracebacks of exceptions raised by TensorFlow code
  is the default behavior.

  Returns:
    True if traceback filtering is enabled
    (e.g. if `tf.debugging.enable_traceback_filtering()` was called),
    and False otherwise (e.g. if `tf.debugging.disable_traceback_filtering()`
    was called).
  """
value = getattr(_ENABLE_TRACEBACK_FILTERING, 'value', True)
exit(value)
