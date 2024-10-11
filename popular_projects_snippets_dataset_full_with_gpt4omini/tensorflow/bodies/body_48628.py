# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
"""Truncates steps per execution to at most one epoch."""
should_truncate = (
    self._inferred_steps is not None and
    self._steps_per_execution_value > self._inferred_steps)
original_value = self._steps_per_execution_value
try:
    if should_truncate:
        self._steps_per_execution.assign(self._inferred_steps)
        self._steps_per_execution_value = self._inferred_steps
    exit()
finally:
    if should_truncate:
        self._steps_per_execution.assign(original_value)
        self._steps_per_execution_value = original_value
