# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
if self._enqueuer:
    self._enqueuer.stop()
self._keras_sequence.on_epoch_end()
