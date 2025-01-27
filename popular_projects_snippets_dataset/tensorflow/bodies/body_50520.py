# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
if self._should_save_on_batch(batch):
    self._save_model(epoch=self._current_epoch, logs=logs)
