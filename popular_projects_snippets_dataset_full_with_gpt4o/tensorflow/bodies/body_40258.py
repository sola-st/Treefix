# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop.py
"""Pushes a new tape onto the tape stack."""
if self._recording:
    raise ValueError("Tape is still recording, This can happen if you try to "
                     "re-enter an already-active tape.")
if self._tape is None:
    self._tape = tape.push_new_tape(
        persistent=self._persistent,
        watch_accessed_variables=self._watch_accessed_variables)
else:
    tape.push_tape(self._tape)
self._recording = True
