# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks.py
# Global step cannot be retrieved via SessionRunArgs and before_run due to
# race condition in hook execution.
global_step = run_context.session.run(self._global_step_tensor)
if global_step >= self._last_step:
    run_context.request_stop()
else:
    self._update_steps_per_run_variable(global_step, run_context.session)
