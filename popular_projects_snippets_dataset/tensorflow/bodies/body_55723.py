# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/experimental/tape.py
"""Enters a context inside which operations are recorded on this tape."""
self._ctx_manager = context_stack.set_default(self._tape_context)
self._ctx_manager.__enter__()
exit(self)
