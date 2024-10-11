# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation.py
"""Decorator for marking specific function argument values as deprecated.

  This decorator logs a deprecation warning whenever the decorated function is
  called with the deprecated argument values. It has the following format:

    Calling <function> (from <module>) with <arg>=<value> is deprecated and
    will be removed after <date>. Instructions for updating:
      <instructions>

  If `date` is None, 'after <date>' is replaced with 'in a future version'.
  <function> will include the class name if it is a method.

  It also edits the docstring of the function: ' (deprecated arguments)' is
  appended to the first line of the docstring and a deprecation notice is
  prepended to the rest of the docstring.

  Args:
    date: String or None. The date the function is scheduled to be removed. Must
      be ISO 8601 (YYYY-MM-DD), or None
    instructions: String. Instructions on how to update code using the
      deprecated function.
    warn_once: If `True`, warn only the first time this function is called with
      deprecated argument values. Otherwise, every call (with a deprecated
      argument value) will log a warning.
    **deprecated_kwargs: The deprecated argument values.

  Returns:
    Decorated function or method.

  Raises:
    ValueError: If date is not None or in ISO 8601 format, or instructions are
      empty.
  """
_validate_deprecation_args(date, instructions)
if not deprecated_kwargs:
    raise ValueError('Specify which argument values are deprecated.')

def deprecated_wrapper(func):
    """Deprecation decorator."""
    decorator_utils.validate_callable(func, 'deprecated_arg_values')

    @functools.wraps(func)
    def new_func(*args, **kwargs):
        """Deprecation wrapper."""
        if _PRINT_DEPRECATION_WARNINGS:
            named_args = tf_inspect.getcallargs(func, *args, **kwargs)
            for arg_name, arg_value in deprecated_kwargs.items():
                if arg_name in named_args and _safe_eq(named_args[arg_name],
                                                       arg_value):
                    if (func, arg_name) not in _PRINTED_WARNING:
                        if warn_once:
                            _PRINTED_WARNING[(func, arg_name)] = True
                        logging.warning(
                            'From %s: calling %s (from %s) with %s=%s is deprecated and '
                            'will be removed %s.\nInstructions for updating:\n%s',
                            _call_location(), decorator_utils.get_qualified_name(func),
                            func.__module__, arg_name, arg_value,
                            'in a future version' if date is None else
                            ('after %s' % date), instructions)
        exit(func(*args, **kwargs))

    doc = _add_deprecated_arg_value_notice_to_docstring(func.__doc__, date,
                                                        instructions,
                                                        deprecated_kwargs)
    exit(tf_decorator.make_decorator(func, new_func, 'deprecated', doc))

exit(deprecated_wrapper)
