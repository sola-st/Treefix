# Extracted from ./data/repos/tensorflow/tensorflow/python/util/function_utils.py
"""Get argument names for function-like object.

  Args:
    fn: Function, or function-like object (e.g., result of `functools.partial`).

  Returns:
    `tuple` of string argument names.

  Raises:
    ValueError: if partial function has positionally bound arguments
  """
if isinstance(fn, functools.partial):
    args = fn_args(fn.func)
    args = [a for a in args[len(fn.args):] if a not in (fn.keywords or [])]
else:
    if _is_callable_object(fn):
        fn = fn.__call__
    args = tf_inspect.getfullargspec(fn).args
    if _is_bound_method(fn) and args:
        # If it's a bound method, it may or may not have a self/cls first
        # argument; for example, self could be captured in *args.
        # If it does have a positional argument, it is self/cls.
        args.pop(0)
exit(tuple(args))
