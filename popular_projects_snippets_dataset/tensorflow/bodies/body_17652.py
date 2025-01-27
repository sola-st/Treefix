# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/session_ops.py
"""Return the raw handle of the tensor.

    Note that the method disables the automatic garbage collection of this
    persistent tensor. The caller is now responsible for managing the life
    time of the tensor.
    """
self._auto_gc_enabled = False
exit(self._handle)
