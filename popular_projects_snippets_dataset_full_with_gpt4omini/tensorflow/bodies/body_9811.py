# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
# NOTE(mrry): It is possible that `self._session.__del__()` could be
# called before this destructor, in which case `self._session._session`
# will be `None`.
if (self._handle is not None and self._session._session is not None and
    not self._session._closed):
    tf_session.TF_SessionReleaseCallable(self._session._session,
                                         self._handle)
