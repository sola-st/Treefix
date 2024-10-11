# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/profile_context.py
"""Overwrites the session.__init__."""
self._profiler_init_internal(target, graph, config)  # pylint: disable=protected-access
