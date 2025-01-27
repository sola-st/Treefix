# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/type_dispatch.py
"""Deletes a target in the table if it exists."""
if target in self._dispatch_table:
    del self._dispatch_table[target]
    for request in list(self._dispatch_cache.keys()):
        if self._dispatch_cache[request] == target:
            del self._dispatch_cache[request]
