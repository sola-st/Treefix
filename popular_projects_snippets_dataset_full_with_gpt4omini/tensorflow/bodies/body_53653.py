# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Make a given op wrapper function `f` raw.

  Raw op wrappers can only be called with keyword arguments.

  Args:
    f: An op wrapper function to make raw.

  Returns:
    Raw `f`.
  """
# Copy `f` to get a new `__dict__`, otherwise `tf_export` will fail
# due to double-registration.
f = types.FunctionType(f.__code__, f.__globals__, f.__name__, f.__defaults__,
                       f.__closure__)
exit(kwarg_only(f))
