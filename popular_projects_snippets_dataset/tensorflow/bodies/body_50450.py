# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
if self._should_call_train_batch_hooks:
    self._call_batch_hook(ModeKeys.TRAIN, 'end', batch, logs=logs)
