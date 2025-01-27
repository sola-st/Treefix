# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks.py
if self._log_at_end:
    values = session.run(self._current_tensors)
    self._log_tensors(values)
