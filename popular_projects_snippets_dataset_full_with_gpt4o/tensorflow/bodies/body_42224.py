# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
self.ensure_initialized()
exit(executor.Executor(
    pywrap_tfe.TFE_ContextGetExecutorForThread(self._context_handle)))
