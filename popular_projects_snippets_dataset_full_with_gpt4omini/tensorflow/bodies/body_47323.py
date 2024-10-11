# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/testing_utils.py
"""Provides a scope within which we compile models to run eagerly or not.

  The boolean gets restored to its original value upon exiting the scope.

  Args:
     value: Bool specifying if we should run models eagerly in the active test.
     Should be True or False.

  Yields:
    The provided value.
  """
previous_value = _thread_local_data.run_eagerly
try:
    _thread_local_data.run_eagerly = value
    exit(value)
finally:
    # Restore model type to initial value.
    _thread_local_data.run_eagerly = previous_value
