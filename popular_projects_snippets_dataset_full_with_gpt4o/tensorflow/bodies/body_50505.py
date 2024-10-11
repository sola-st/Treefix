# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
if not self._called_in_fit:
    self._finalize_progbar(logs, self._test_step)
