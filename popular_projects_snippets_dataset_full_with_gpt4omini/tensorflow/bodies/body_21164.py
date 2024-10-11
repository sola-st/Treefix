# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session.py
"""Creates a `_WrappedSession`.

    Args:
      sess: A `tf.compat.v1.Session` or `_WrappedSession` object.  The wrapped
        session.
    """
self._sess = sess
self._wrapped_is_stoppable = isinstance(self._sess, _WrappedSession)
