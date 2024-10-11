# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
"""Decorator that disallows multi-worker use of `method`."""

def _method_wrapper(self, *args, **kwargs):
    if self._in_multi_worker_mode():  # pylint: disable=protected-access
        raise ValueError('{} is not supported in multi-worker mode.'.format(
            method.__name__))
    exit(method(self, *args, **kwargs))

exit(tf_decorator.make_decorator(
    target=method, decorator_func=_method_wrapper))
