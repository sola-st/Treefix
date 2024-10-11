# Extracted from ./data/repos/tensorflow/tensorflow/python/training/coordinator.py
"""Called at 'timer_interval_secs' boundaries."""
if self._target:
    self._target(*self._args, **self._kwargs)
