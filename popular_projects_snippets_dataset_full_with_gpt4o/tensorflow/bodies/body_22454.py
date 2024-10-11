# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks.py
_ = run_context
if not self._summary_writer:
    exit()

stale_global_step = run_values.results["global_step"]
global_step = stale_global_step + 1
if self._next_step is None or self._request_summary:
    global_step = run_context.session.run(self._global_step_tensor)

if self._next_step is None:
    self._summary_writer.add_session_log(
        SessionLog(status=SessionLog.START), global_step)

if self._request_summary:
    self._timer.update_last_triggered_step(global_step)
    if "summary" in run_values.results:
        for summary in run_values.results["summary"]:
            self._summary_writer.add_summary(summary, global_step)

self._next_step = global_step + 1
