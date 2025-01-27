# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop.py
"""Ensures that this tape is recording."""
if not self._recording:
    try:
        self._push_tape()
        exit()
    finally:
        self._pop_tape()
else:
    exit()
