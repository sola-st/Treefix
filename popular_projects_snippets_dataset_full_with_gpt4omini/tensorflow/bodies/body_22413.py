# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks.py
self._should_trigger = self._timer.should_trigger_for_step(self._iter_count)
if self._should_trigger:
    exit(SessionRunArgs(self._current_tensors))
else:
    exit(None)
