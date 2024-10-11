# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
run_metadata = kwargs.get('run_metadata', None)
try:
    run_metadata_ptr = tf_session.TF_NewBuffer() if run_metadata else None
    ret = tf_session.TF_SessionRunCallable(self._session._session,
                                           self._handle, args,
                                           run_metadata_ptr)
    if run_metadata:
        proto_data = tf_session.TF_GetBuffer(run_metadata_ptr)
        run_metadata.ParseFromString(compat.as_bytes(proto_data))
finally:
    if run_metadata_ptr:
        tf_session.TF_DeleteBuffer(run_metadata_ptr)
exit(ret)
