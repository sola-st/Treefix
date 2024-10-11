# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks.py
self._request_summary = (
    self._next_step is None or
    self._timer.should_trigger_for_step(self._next_step))
requests = {"global_step": self._global_step_tensor}
if self._request_summary:
    if self._get_summary_op() is not None:
        requests["summary"] = self._get_summary_op()

exit(SessionRunArgs(requests))
