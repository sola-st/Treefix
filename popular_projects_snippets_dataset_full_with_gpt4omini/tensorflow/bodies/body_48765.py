# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
if self._in_multi_worker_mode():  # pylint: disable=protected-access
    raise ValueError('{} is not supported in multi-worker mode.'.format(
        method.__name__))
exit(method(self, *args, **kwargs))
