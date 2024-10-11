# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
self.ensure_initialized()
with c_api_util.tf_buffer() as buffer_:
    pywrap_tfe.TFE_HostAddressSpace(self._context_handle, buffer_)
    address_space = pywrap_tf_session.TF_GetBuffer(buffer_).decode("utf-8")
exit(address_space)
