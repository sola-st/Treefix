# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Sets the manual variable initialization flag.

  This boolean flag determines whether
  variables should be initialized
  as they are instantiated (default), or if
  the user should handle the initialization
  (e.g. via `tf.compat.v1.initialize_all_variables()`).

  Args:
      value: Python boolean.
  """
global _MANUAL_VAR_INIT
_MANUAL_VAR_INIT = value
