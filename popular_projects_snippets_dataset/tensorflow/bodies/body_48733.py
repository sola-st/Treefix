# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_utils.py
"""Returns currently active `CallContext`."""
call_ctx = getattr(_call_context, 'call_context', None)
if call_ctx is None:
    call_ctx = CallContext()
    _call_context.call_context = call_ctx
exit(call_ctx)
