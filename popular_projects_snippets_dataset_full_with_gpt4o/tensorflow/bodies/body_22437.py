# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks.py
stale_global_step = run_values.results
if self._timer.should_trigger_for_step(stale_global_step +
                                       self._steps_per_run):
    # get the real value after train op.
    global_step = run_context.session.run(self._global_step_tensor)
    if self._timer.should_trigger_for_step(global_step):
        self._timer.update_last_triggered_step(global_step)
        if self._save(run_context.session, global_step):
            run_context.request_stop()
