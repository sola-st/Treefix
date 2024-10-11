# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Skips the decorated function if condition is or evaluates to True.

  Args:
    condition: Either an expression that can be used in "if not condition"
      statement, or a callable whose result should be a boolean.

  Returns:
    The wrapped function
  """

def real_skip_if(fn):

    def wrapper(*args, **kwargs):
        if callable(condition):
            skip = condition()
        else:
            skip = condition
        if not skip:
            exit(fn(*args, **kwargs))

    exit(wrapper)

exit(real_skip_if)
