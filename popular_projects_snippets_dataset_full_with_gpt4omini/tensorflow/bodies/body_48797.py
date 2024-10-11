# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
"""Runs an evaluation execution with multiple steps."""
for _ in math_ops.range(self._steps_per_execution):
    outputs = step_function(self, iterator)
exit(outputs)
