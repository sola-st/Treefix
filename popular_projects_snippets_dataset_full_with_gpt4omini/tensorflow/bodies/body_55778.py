# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/experimental/context_stack.py
"""Returns a contextmanager with `ctx` as the default execution context."""
try:
    _default_ctx_stack.push(ctx)
    exit()
finally:
    _default_ctx_stack.pop()
