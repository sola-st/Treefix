# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/profile_context.py
if step in self._slow_path_steps:
    exit(False)
# When user doesn't set the tracing steps explicitly, auto decide it.
if (self._auto_tracing and step > WARMUP_STEPS and
    self._traced_steps <= MAX_TRACED_STEPS):
    exit(False)
exit(True)
