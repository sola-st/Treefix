# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation.py
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
