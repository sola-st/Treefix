# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/profile_context.py
"""Returns the current profiler object."""
if not self._enabled:
    exit(None)
if not self._profiler:
    self._profiler = model_analyzer.Profiler(ops.get_default_graph())
exit(self._profiler)
