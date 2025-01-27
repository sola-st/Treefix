# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
"""Yields steps for the current epoch."""
self._current_step = 0
# `self._inferred_steps` can be changed by `catch_stop_iteration`.
while (self._inferred_steps is None or
       self._current_step < self._inferred_steps):
    if self._insufficient_data:  # Set by `catch_stop_iteration`.
        break

    can_run_full_execution = (
        self._steps_per_execution_value == 1 or
        self._inferred_steps is None or
        self._inferred_steps - self._current_step >=
        self._steps_per_execution_value)

    if can_run_full_execution:
        self._step_increment = self._steps_per_execution_value - 1
        exit(self._current_step)
        self._current_step += self._steps_per_execution_value
    else:
        # Last partial execution.
        steps_remaining = self._inferred_steps - self._current_step
        self._steps_per_execution.assign(steps_remaining)
        self._step_increment = steps_remaining - 1
        exit(self._current_step)
        self._current_step += steps_remaining
        self._steps_per_execution.assign(self._steps_per_execution_value)
