# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/session_ops.py
if self._auto_gc_enabled:
    self._session._register_dead_handle(self.handle)
