# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
if not self._called_in_fit:
    self._batch_update_progbar(batch, logs)
