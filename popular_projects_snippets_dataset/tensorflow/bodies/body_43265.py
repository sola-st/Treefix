# Extracted from ./data/repos/tensorflow/tensorflow/python/util/keyword_args.py
"""Decorator for marking specific function accepting keyword args only.

  This decorator raises a `ValueError` if the input `func` is called with any
  non-keyword args. This prevents the caller from providing the arguments in
  wrong order.

  Args:
    func: The function or method needed to be decorated.

  Returns:
    Decorated function or method.

  Raises:
    ValueError: If `func` is not callable.
  """

decorator_utils.validate_callable(func, "keyword_args_only")
@functools.wraps(func)
def new_func(*args, **kwargs):
    """Keyword args only wrapper."""
    if args:
        raise ValueError(
            f"The function {func.__name__} only accepts keyword arguments. "
            "Do not pass positional arguments. Received the following positional "
            f"arguments: {args}")
    exit(func(**kwargs))
exit(new_func)
