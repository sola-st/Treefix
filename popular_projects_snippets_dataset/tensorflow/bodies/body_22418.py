# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks.py
"""Initializes a `MultiStepStopAtStepHook`.

    This hook requests stop after either a number of steps have been
    executed or a last step has been reached. Only one of the two options can be
    specified.

    if `num_steps` is specified, it indicates the number of steps to execute
    after `begin()` is called. If instead `last_step` is specified, it
    indicates the last step we want to execute, as passed to the `after_run()`
    call.

    In Estimator, the user provided computation, the model_fn, is wrapped
    inside a tf.while_loop for peak performance. The steps_per_run variable
    determines the number of iterations of the loop before returning to the CPU.

    Args:
      num_steps: Number of steps to execute.
      last_step: Step after which to stop.
      steps_per_run: Number of steps executed per run call.

    Raises:
      ValueError: If one of the arguments is invalid.
    """
if num_steps is None and last_step is None:
    raise ValueError("One of num_steps or last_step must be specified.")
if num_steps is not None and last_step is not None:
    raise ValueError("Only one of num_steps or last_step can be specified.")
if steps_per_run is None or steps_per_run < 1:
    raise ValueError("steps_per_run should be greater than 0")
self._num_steps = num_steps
self._last_step = last_step
self._steps_per_run_initial_value = steps_per_run
