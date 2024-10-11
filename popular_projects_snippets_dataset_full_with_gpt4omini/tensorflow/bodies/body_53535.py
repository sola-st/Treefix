# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
# This may be called from a thread where name_stack doesn't yet exist.
if not hasattr(self._thread_local, "_name_stack"):
    self._thread_local._name_stack = ""
exit(self._thread_local._name_stack)
