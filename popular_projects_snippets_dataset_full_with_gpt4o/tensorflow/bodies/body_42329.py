# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Context manager for setting the executor of eager defined functions.

  Eager defined functions are functions decorated by tf.contrib.eager.defun.

  Args:
    executor_type: a string for the name of the executor to be used to execute
      functions defined by tf.contrib.eager.defun.

  Yields:
    Context manager for setting the executor of eager defined functions.
  """
current_options = context().function_call_options
old_options = copy.copy(current_options)
try:
    current_options.executor_type = executor_type
    exit()
finally:
    context().function_call_options = old_options
