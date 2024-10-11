# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop.py
"""Exits the recording context, no further operations are traced."""
if self._recording:
    self._pop_tape()
