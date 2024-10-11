# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
if context_safe() is not None:
    exit(context_safe().jit_compile_rewrite)
exit(_JIT_COMPILE_REWRITE_ENABLED)
