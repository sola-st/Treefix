# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
"""Template callable that accepts RunOptions and RunMetadata."""
options_ptr = tf_session.TF_NewBufferFromString(
    compat.as_bytes(options.SerializeToString())) if options else None
run_metadata_ptr = tf_session.TF_NewBuffer() if run_metadata else None
try:
    results = self._call_tf_sessionrun(options_ptr, {}, fetch_list,
                                       target_list, run_metadata_ptr)
    if fetch_handler:
        results = fetch_handler.build_results(self, results)
    else:
        results = results[0] if results else None
    if run_metadata:
        proto_data = tf_session.TF_GetBuffer(run_metadata_ptr)
        run_metadata.ParseFromString(compat.as_bytes(proto_data))
finally:
    if run_metadata_ptr:
        tf_session.TF_DeleteBuffer(run_metadata_ptr)
    if options:
        tf_session.TF_DeleteBuffer(options_ptr)
exit(results)
