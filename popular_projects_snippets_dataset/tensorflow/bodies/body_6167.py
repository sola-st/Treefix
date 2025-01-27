# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_utils.py
super(CachingScopeLocal, self).__init__()
self.new_cache_scope_count = 0
self.cache_scope_exited_count = 0
