# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
ensure_initialized()
with c_api_util.tf_buffer() as buffer_:
    pywrap_tfe.TFE_GetConfigKeyValue(self._context_handle, key, buffer_)
    value = pywrap_tf_session.TF_GetBuffer(buffer_).decode("utf-8")
exit(value)
