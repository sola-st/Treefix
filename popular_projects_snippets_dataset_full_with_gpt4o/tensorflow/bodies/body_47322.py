# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/testing_utils.py
"""Provides a scope within which the model type to test is equal to `value`.

  The model type gets restored to its original value upon exiting the scope.

  Args:
     value: model type value

  Yields:
    The provided value.
  """
previous_value = _thread_local_data.model_type
try:
    _thread_local_data.model_type = value
    exit(value)
finally:
    # Restore model type to initial value.
    _thread_local_data.model_type = previous_value
