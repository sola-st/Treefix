# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
if self._context_handle is not None:
    pywrap_tfe.TFE_ContextSetJitCompileRewrite(self._handle, enable)
self._jit_compile_rewrite = enable
