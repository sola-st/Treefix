# Extracted from ./data/repos/tensorflow/tensorflow/python/util/lazy_loader.py
self._local_name = local_name
self._parent_module_globals = parent_module_globals
self._warning = warning

super(LazyLoader, self).__init__(name)
