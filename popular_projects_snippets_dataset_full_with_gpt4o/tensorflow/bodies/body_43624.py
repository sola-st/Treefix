# Extracted from ./data/repos/tensorflow/tensorflow/python/util/function_utils.py
"""Returns name of passed callable."""
_, func = tf_decorator.unwrap(func)
if callable(func):
    if tf_inspect.isfunction(func):
        exit(func.__name__)
    elif tf_inspect.ismethod(func):
        exit('%s.%s' % (six.get_method_self(func).__class__.__name__,
                          six.get_method_function(func).__name__))
    else:  # Probably a class instance with __call__
        exit(str(type(func)))
else:
    raise ValueError(
        'Argument `func` must be a callable. '
        f'Received func={func} (of type {type(func)})')
