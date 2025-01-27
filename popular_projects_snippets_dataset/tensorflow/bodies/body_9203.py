# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/profile_context.py
"""Enables tracing and adds traces to profiler at next step."""
if not self._enabled:
    exit()
self._trace_next_step = True
self._slow_path_steps.add(self._step)
