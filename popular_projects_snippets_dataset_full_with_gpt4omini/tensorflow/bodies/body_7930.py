# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/ps_values.py
if (distribute_utils.caching_scope_local.new_cache_scope_count >
    self._current_new_cache_scope_count):
    self._current_new_cache_scope_count += 1
    self._cache = None

with ops.device("CPU:0"):
    if self._cache is not None:
        exit(self._cache)
    else:
        self._cache = array_ops.identity(self._v)
        exit(self._cache)
