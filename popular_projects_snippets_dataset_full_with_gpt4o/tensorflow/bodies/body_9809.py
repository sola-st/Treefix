# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
self._session = session
self._handle = None
options_ptr = tf_session.TF_NewBufferFromString(
    compat.as_bytes(callable_options.SerializeToString()))
try:
    self._handle = tf_session.TF_SessionMakeCallable(
        session._session, options_ptr)
finally:
    tf_session.TF_DeleteBuffer(options_ptr)
