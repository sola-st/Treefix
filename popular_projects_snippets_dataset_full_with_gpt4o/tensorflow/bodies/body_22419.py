# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks.py
self._global_step_tensor = training_util.get_global_step()
if self._global_step_tensor is None:
    raise RuntimeError("Global step should be created to use StopAtStepHook.")
self._steps_per_run_variable = get_or_create_steps_per_run_variable()
