# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session.py
"""Create a new `_RecoverableSession`.

    The value returned by calling `sess_creator.create_session()` will be the
    session wrapped by this recoverable session.

    Args:
      sess_creator: A 'SessionCreator' to be wrapped by recoverable.
    """
self._sess_creator = sess_creator
_WrappedSession.__init__(self, self._create_session())
