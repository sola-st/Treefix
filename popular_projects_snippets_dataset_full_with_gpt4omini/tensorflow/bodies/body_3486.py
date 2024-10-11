# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/type_dispatch.py
"""Caches the dispatch lookup result for a target."""
if target is not None:
    # LRU Cache removes oldest item
    if len(self._dispatch_cache) > _MAX_DISPATCH_CACHE:
        self._dispatch_cache.popitem(last=False)
    self._dispatch_cache[request] = target
