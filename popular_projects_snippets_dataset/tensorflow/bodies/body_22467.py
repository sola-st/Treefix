# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks.py
self._request_summary = (
    self._next_step is not None and
    self._timer.should_trigger_for_step(self._next_step))
requests = {"global_step": self._global_step_tensor}
opts = (
    config_pb2.RunOptions(trace_level=config_pb2.RunOptions.FULL_TRACE)
    if self._request_summary else None)

exit(SessionRunArgs(requests, options=opts))
