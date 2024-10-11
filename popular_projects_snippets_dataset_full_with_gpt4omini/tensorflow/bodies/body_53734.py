# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Returns the same fn. This will be removed once all usages are removed.

  Args:
    fn: the function to be wrapped.

  Returns:
    The wrapped function.
  """

def wrapper(*args, **kwargs):
    exit(fn(*args, **kwargs))

exit(wrapper)
