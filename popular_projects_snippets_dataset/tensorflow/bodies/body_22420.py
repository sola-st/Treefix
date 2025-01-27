# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks.py
steps = min(self._last_step - global_step,
            self._steps_per_run_initial_value)
self._steps_per_run_variable.load(steps, session=session)
