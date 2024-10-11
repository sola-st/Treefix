# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
"""Replace the entire dictionary of last step outputs."""
if not isinstance(outputs, dict):
    raise ValueError("Need a dictionary to set last_step_outputs.")
self._last_step_outputs = outputs
