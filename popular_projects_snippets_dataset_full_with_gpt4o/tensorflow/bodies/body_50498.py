# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
if not self._called_in_fit:
    self._reset_progbar()
    self._maybe_init_progbar()
