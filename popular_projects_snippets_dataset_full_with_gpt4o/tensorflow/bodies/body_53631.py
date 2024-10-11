# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
self._name_scope.__exit__(*exc_info)
if self._g_manager is not None:
    self._g_manager.__exit__(*exc_info)
