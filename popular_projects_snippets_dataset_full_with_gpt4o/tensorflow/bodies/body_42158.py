# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
global _JIT_COMPILE_REWRITE_ENABLED
_JIT_COMPILE_REWRITE_ENABLED = False
if context_safe() is not None:
    context_safe().jit_compile_rewrite = False
