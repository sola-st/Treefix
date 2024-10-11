# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks.py
global_step = run_values.results + 1
if global_step >= self._last_step:
    # Check latest global step to ensure that the targeted last step is
    # reached. global_step read tensor is the value of global step
    # before running the operation. We're not sure whether current session.run
    # incremented the global_step or not. Here we're checking it.

    step = run_context.session.run(self._global_step_tensor)
    if step >= self._last_step:
        run_context.request_stop()
