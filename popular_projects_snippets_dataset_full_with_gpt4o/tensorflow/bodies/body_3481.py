# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/type_dispatch.py
"""Adds a new target type."""
self._dispatch_table[target] = None
for request in self._dispatch_cache:
    if target.is_supertype_of(self._dispatch_cache[request]):
        self._dispatch_cache[request] = target
