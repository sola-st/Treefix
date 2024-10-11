# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
self.ensure_initialized()
pywrap_tfe.TFE_ContextSetExecutorForThread(self._context_handle, e.handle())
