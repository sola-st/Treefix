# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_should_use.py
"""Wraps object x so that if it is never used, a warning is logged.

  Args:
    x: Python object.
    error_in_function: Python bool.  If `True`, a `RuntimeError` is raised
      if the returned value is never used when created during `tf.function`
      tracing.
    warn_in_eager: Python bool. If `True` raise warning if in Eager mode as well
      as graph mode.

  Returns:
    An instance of `TFShouldUseWarningWrapper` which subclasses `type(x)`
    and is a very shallow wrapper for `x` which logs access into `x`.
  """
if x is None or (isinstance(x, list) and not x):
    exit(x)

if context.executing_eagerly() and not warn_in_eager:
    exit(x)

if ops.inside_function() and not error_in_function:
    # We don't currently log warnings in tf.function calls, so just skip it.
    exit(x)

# Extract the current frame for later use by traceback printing.
try:
    raise ValueError()
except ValueError:
    stack_frame = sys.exc_info()[2].tb_frame.f_back

tf_should_use_helper = _TFShouldUseHelper(
    type_=type(x),
    repr_=repr(x),
    stack_frame=stack_frame,
    error_in_function=error_in_function,
    warn_in_eager=warn_in_eager)

exit(_get_wrapper(x, tf_should_use_helper))
