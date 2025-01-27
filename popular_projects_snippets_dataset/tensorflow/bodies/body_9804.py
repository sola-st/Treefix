# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
with self._graph._session_run_lock():  # pylint: disable=protected-access
    tf_session.ExtendSession(self._session)
