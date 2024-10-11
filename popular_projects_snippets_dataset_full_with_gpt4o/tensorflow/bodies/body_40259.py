# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop.py
if not self._recording:
    raise ValueError("Tape is not recording.")
tape.pop_tape(self._tape)
self._recording = False
