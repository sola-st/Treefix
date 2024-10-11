# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
with _context_lock:
    if _context is None:
        ctx = Context()
        _set_context_locked(ctx)
