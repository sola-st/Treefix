# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
# cleanly ignore all exceptions
try:
    self.close()
except Exception:  # pylint: disable=broad-except
    pass
if self._session is not None:
    try:
        tf_session.TF_DeleteSession(self._session)
    except (AttributeError, TypeError):
        # At shutdown, `c_api_util`, `tf_session`, or
        # `tf_session.TF_DeleteSession` may have been garbage collected, causing
        # the above method calls to fail. In this case, silently leak since the
        # program is about to terminate anyway.
        pass
    self._session = None
