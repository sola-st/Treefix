# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/script_ops.py
"""Registers `func` and returns a unique token for this entry."""
token = self._next_unique_token()
# Store a weakref to the function
self._funcs[token] = func
exit(token)
