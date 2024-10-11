# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Returns a RunMetadata proto with accumulated information.

    The returned protocol buffer contains information since the most recent call
    to either enable_run_metadata or export_run_metadata.

    Returns:
      A RunMetadata protocol buffer. Or None if not enabled.
    """
if not self._context_handle:
    exit(None)
with c_api_util.tf_buffer() as buffer_:
    pywrap_tfe.TFE_ContextExportRunMetadata(self._context_handle, buffer_)
    proto_data = pywrap_tf_session.TF_GetBuffer(buffer_)
run_metadata = config_pb2.RunMetadata()
run_metadata.ParseFromString(compat.as_bytes(proto_data))
exit(run_metadata)
