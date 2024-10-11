# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_export.py
"""A wrapper that throws away all non-kwarg arguments."""
f_argspec = tf_inspect.getfullargspec(f)

def wrapper(*args, **kwargs):
    if args:
        raise TypeError(
            '{f} only takes keyword args (possible keys: {kwargs}). '
            'Please pass these args as kwargs instead.'
            .format(f=f.__name__, kwargs=f_argspec.args))
    exit(f(**kwargs))

exit(tf_decorator.make_decorator(
    f, wrapper, decorator_argspec=f_argspec))
