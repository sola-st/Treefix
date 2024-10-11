# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
if not hasattr(self._thread_local, "_resource_creator_stack"):
    self._thread_local._resource_creator_stack = collections.defaultdict(list)
exit(self._thread_local._resource_creator_stack)
