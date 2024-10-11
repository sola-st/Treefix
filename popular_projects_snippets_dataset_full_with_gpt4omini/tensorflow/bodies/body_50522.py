# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
self.epochs_since_last_save += 1
# pylint: disable=protected-access
if self.save_freq == 'epoch':
    self._save_model(epoch=epoch, logs=logs)
