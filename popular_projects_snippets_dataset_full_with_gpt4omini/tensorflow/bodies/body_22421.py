# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks.py
global_step = session.run(self._global_step_tensor)
if self._last_step is None:
    self._last_step = global_step + self._num_steps
self._update_steps_per_run_variable(global_step, session)
