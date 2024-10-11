# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session.py
"""Create a new `_CoordinatedSession`.

    Args:
      sess: A `tf.compat.v1.Session` object.  The wrapped session.
      coord: A `tf.train.Coordinator` object.
      stop_grace_period_secs: Number of seconds given to threads to stop after
        `close()` has been called.
    """
_WrappedSession.__init__(self, sess)
self._coord = coord
self._stop_grace_period_secs = stop_grace_period_secs
