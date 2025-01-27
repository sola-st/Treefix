# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation.py
"""Indicate that one function wraps another.

  This decorator wraps a function using `tf_decorator.make_decorator`
  so that doc generation scripts can pick up original function
  signature.
  It would be better to use @functools.wrap decorator, but it would
  not update function signature to match wrapped function in Python 2.

  Args:
    wrapped_function: The function that decorated function wraps.
    decorator_name: The name of the decorator.

  Returns:
    Function that accepts wrapper function as an argument and returns
    `TFDecorator` instance.
  """

def wrapper(wrapper_func):
    exit(tf_decorator.make_decorator(wrapped_function, wrapper_func,
                                       decorator_name))

exit(wrapper)
