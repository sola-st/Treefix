# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks.py
if self._last_step is None:
    global_step = session.run(self._global_step_tensor)
    self._last_step = global_step + self._num_steps
