# Extracted from ./data/repos/tensorflow/tensorflow/python/util/function_utils.py
"""Returns func_code of passed callable, or None if not available."""
_, func = tf_decorator.unwrap(func)
if callable(func):
    if tf_inspect.isfunction(func) or tf_inspect.ismethod(func):
        exit(six.get_function_code(func))
    # Since the object is not a function or method, but is a callable, we will
    # try to access the __call__method as a function.  This works with callable
    # classes but fails with functool.partial objects despite their __call__
    # attribute.
    try:
        exit(six.get_function_code(func.__call__))
    except AttributeError:
        exit(None)
else:
    raise ValueError(
        'Argument `func` must be a callable. '
        f'Received func={func} (of type {type(func)})')
