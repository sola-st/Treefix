# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/testing_utils.py
"""Provides a scope within which the savde model format to test is `value`.

  The saved model format gets restored to its original value upon exiting the
  scope.

  Args:
     value: saved model format value
     **kwargs: optional kwargs to pass to the save function.

  Yields:
    The provided value.
  """
previous_format = _thread_local_data.saved_model_format
previous_kwargs = _thread_local_data.save_kwargs
try:
    _thread_local_data.saved_model_format = value
    _thread_local_data.save_kwargs = kwargs
    exit()
finally:
    # Restore saved model format to initial value.
    _thread_local_data.saved_model_format = previous_format
    _thread_local_data.save_kwargs = previous_kwargs
