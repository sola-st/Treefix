# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Run jit_compile functions through rewrite pass.

  This runs jit_compile functions through all of the multidevice function
  rewrite passes.
  """
global _JIT_COMPILE_REWRITE_ENABLED
_JIT_COMPILE_REWRITE_ENABLED = True
if context_safe() is not None:
    context_safe().jit_compile_rewrite = True
