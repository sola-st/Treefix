# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
# If the context was already initialized, publish it. Otherwise wait with
# publication until it's initialized.
if self._initialized:
    pywrap_tfe.TFE_Py_SetCEagerContext(self._context_handle)
self._is_global_context = True
