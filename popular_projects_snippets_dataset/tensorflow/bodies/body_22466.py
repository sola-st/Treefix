# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks.py
self._next_step = None
self._global_step_tensor = training_util._get_or_create_global_step_read()  # pylint: disable=protected-access
if self._global_step_tensor is None:
    raise RuntimeError("Global step should be created to use ProfilerHook.")
