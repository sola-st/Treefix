# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks.py
stale_global_step = run_values.results["global_step"]
if self._next_step is None:
    # Update the timer so that it does not activate until N steps or seconds
    # have passed.
    self._timer.update_last_triggered_step(stale_global_step)
global_step = stale_global_step + 1
if self._request_summary:
    global_step = run_context.session.run(self._global_step_tensor)
    self._timer.update_last_triggered_step(global_step)
    self._save(global_step, self._output_file.format(global_step),
               run_values.run_metadata.step_stats)
    self._file_writer.add_run_metadata(run_values.run_metadata,
                                       "step_%d" % global_step)

self._next_step = global_step + 1
