# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
"""Calls the `on_train_batch_begin` methods of its callbacks.

    Args:
        batch: Integer, index of batch within the current epoch.
        logs: Dict, contains the return value of `model.train_step`. Typically,
          the values of the `Model`'s metrics are returned.  Example:
          `{'loss': 0.2, 'accuracy': 0.7}`.
    """
if self._should_call_train_batch_hooks:
    self._call_batch_hook(ModeKeys.TRAIN, 'begin', batch, logs=logs)
