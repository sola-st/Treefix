# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
if _tensor_caches_map is None:
    exit()
if self._context_id in _tensor_caches_map:
    del _tensor_caches_map[self._context_id]
