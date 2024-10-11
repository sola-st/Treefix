# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
if self._count == 0:
    raise errors_impl.AbortedError('Aborted at N', None, None)
self._count -= 1
exit(self._sess.run(*args, **kwargs))
