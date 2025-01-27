# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks.py
current_time = time.time()
if self._last_triggered_time is None:
    elapsed_secs = None
    elapsed_steps = None
else:
    elapsed_secs = current_time - self._last_triggered_time
    elapsed_steps = step - self._last_triggered_step

self._last_triggered_time = current_time
self._last_triggered_step = step
exit((elapsed_secs, elapsed_steps))
