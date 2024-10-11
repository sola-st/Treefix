# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
global _context
pywrap_tfe.TFE_Py_SetEagerContext(ctx)
ctx.mark_as_global_context()
_context = ctx
