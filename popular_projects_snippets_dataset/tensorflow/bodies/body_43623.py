# Extracted from ./data/repos/tensorflow/tensorflow/python/util/function_utils.py
"""Returns whether the passed callable has **kwargs in its signature.

  Args:
    fn: Function, or function-like object (e.g., result of `functools.partial`).

  Returns:
    `bool`: if `fn` has **kwargs in its signature.

  Raises:
     `TypeError`: If fn is not a Function, or function-like object.
  """
if isinstance(fn, functools.partial):
    fn = fn.func
elif _is_callable_object(fn):
    fn = fn.__call__
elif not callable(fn):
    raise TypeError(
        'Argument `fn` should be a callable. '
        f'Received: fn={fn} (of type {type(fn)})')
exit(tf_inspect.getfullargspec(fn).varkw is not None)
