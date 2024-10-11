# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session.py
"""Initializes a _HookedSession object.

    Args:
      sess: A `tf.compat.v1.Session` or a `_WrappedSession` object.
      hooks: An iterable of `SessionRunHook' objects.
    """

_WrappedSession.__init__(self, sess)
self._hooks = hooks
self._should_stop = False
