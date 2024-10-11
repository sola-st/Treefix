# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks.py
_ = run_context
if self._should_trigger:
    self._log_tensors(run_values.results)

self._iter_count += 1
